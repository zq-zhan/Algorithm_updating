import paddle
import paddle.nn as nn
import paddle.nn.functiional as F


class PLELayer(nn.Layer):
    def __init__(self, feature_size, task_num, exp_per_task, shared_num,
                 expert_size, tower_size, level_number):
        """
            关键维度:
                B: batch_size
                F: feature_size 输入特征维度
                T: task_num 任务数
                p: exp_per_task 每个任务的私有专家数
                s: shared_num 共享专家数
                E: expert_size 每个专家的输出维度
                H: tower_size tower隐层大小
                L: level_number ple层数
        """
        super().__init__()

        self.task_num = task_num
        self.exp_per_task = exp_per_task
        self.shared_num = shared_num
        self.expert_size = expert_size
        self.tower_size = tower_size
        self.level_number = level_number

        # ple层
        self.ple_layers = []
        for i in range(0, self.level_number):
            if i == self.level_number - 1:
                ple_layer = self.add_sublayer(
                    name = 'lev_' + str(i),
                    sublayer = SinglePLELayer(
                        feature_size, task_num, exp_per_task, shared_num, 
                        expert_size, 'lev_' + str(i), True)
                    )
                self.ple_layers.append(ple_layer)
                break
            else:
                ple_layer = self.add_sublayer(
                    name = 'lev_' + str(i),
                    sublayer = SinglePLELayer(
                        feature_size, task_num, exp_per_task, shared_num, 
                        expert_size, 'lev_' + str(i), False)
                    )
                self.ple_layers.append(ple_layer)
                feature_size = expert_size # 第一层输入为feature_size, 后续层输入为expert_size

        # tower层   
        self._param_tower = []
        self._param_tower_out = []
        task_init = [pow(10, -i) for i in range(1, self.task_num + 1)]
        for i in range(0, self.task_num):
            linear = self.add_sublayer(
                name = 'tower_' + str(i),
                sublayer = nn.Linear(
                    expert_size,
                    tower_size,
                    weight_attr = nn.initializer.Constant(value = task_init[i]),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = 'tower_' + str(i)
                )
            )
            self._param_tower.append(linear)

            linear = self.add_sublayer(
                name = 'tower_out_' + str(i),
                sublayer = nn.Linear(
                    tower_size,
                    2,
                    weight_attr = nn.initializer.Constant(value = task_init[i]),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = 'tower_out_' + str(i)
                )
            )
            self._param_tower_out.append(linear)
    
    def forward(self, input_data):
        # input_data: [B, F]
        input_ple = [] # [B, F, T + 1]
        # 分别用于task_num个的私有专家网络输入变换，以及共享专家网络的输入变换
        for i in range(0, self.task_num + 1):
            input_ple.append(input_data)
        # ple层
        ple_out = []
        for i in range(0, self.level_number):
            ple_out = self.ple_layers[i](input_ple) # T + 1个[B, E] -> T个[B, E]
            input_ple = ple_out
        
        # tower层
        output_layers = []
        for i in range(0, self.task_num):
            cur_tower = self._param_tower[i](ple_out[i]) # 输入:[B, E], 输出：[B, H]
            cur_tower = F.relu(cur_tower)
            out = self._param_tower_out[i](cur_tower) # 输入:[B, H], 输出：[B, 2]
            out = F.softmax(out, axis = 1)
            out = paddle.clip(out, min = 1e-10, max = 1.0 - 1e-10)
            output_layers.append(out) # 列表,T个[B, 2]
        
        return output_layers # 列表,T个[B, 2]


class SinglePLELayer(nn.Layer):
    def __init__(self, input_feature_size, task_num, exp_per_task, share_num,
                 expert_size, level_name, if_last):
        """
            input_feature_size: 输入特征维度
            task_num: 任务数
            exp_per_task: 每个任务的私有专家数
            share_num: 共享专家数
            expert_size: 每个专家的输出维度
            level_name: 网络名称
            if_last: 是否是最后一层
        """
        super().__init__()
        
        self.task_num = task_num
        self.exp_per_task = exp_per_task
        self.share_num = share_num
        self.expert_size = expert_size
        self.level_name = level_name

        self._param_expert = []
        # 私有专家网络
        step = self.exp_per_task
        for i in range(self.task_num):
            exp_init = [
                pow(10, -k) for k in range(1 + i + step, step * (i + 1) + 1) 
            ]
            for j in range(0, self.exp_per_task):
                linear= self.add_sublayer(
                    name = level_name + '_exp_' + str(i) + '_' + str(j),
                    sublayer = nn.Linear(
                        input_feature_size,
                        expert_size,
                        weight_attr = nn.initializer.Constant(value = exp_init[j]),
                        bias_attr = nn.initializer.Constant(value = 0.1),
                        name = level_name + '_exp_' + str(i) + '_' + str(j)
                    )
                )
                self._param_expert.append(linear)

        # 共享专家网络
        shared_exp_init = [pow(10, -i) for i in range(1, self.shared_num + 1)]
        for i in range(self.shared_num):
            linear = self.add_sublayer(
                name = level_name + '_exp_shared' + str(i),
                sublayer = nn.Linear(
                    input_feature_size,
                    expert_size,
                    weight_attr = nn.initializer.Constant(value = shared_exp_init[i]),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = level_name + '_exp_shared' + str(i)
                )
            )
            self._param_expert.append(linear)

        # task gate, 每个任务有各自的gate
        self._param_gate = []
        cur_expert_num = self.exp_per_task + self.shared_num # 当前专家数=私有专家数+共享专家数
        gate_init = [pow(10, -i) for i in range(1, self.task_num + 1)]
        for i in range(self.task_num):
            linear = self.add_sublayer(
                name = level_name + '_gate_' + str(i),
                sublayer = nn.Linear(
                    input_feature_size,
                    cur_expert_num, # p + s
                    weight_attr = nn.initializer.Constant(value = gate_init[i]),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = level_name + '_gate_' + str(i)
                )
            )
            self._param_gate.append(linear)
        
        # shared gate, 不是最后一层才有
        if not if_last:
            cur_expert_num = self.task_num * self.exp_per_task + self.share_num
            linear = self.add_sublayer(
                name = level_name + '_gate_shared_',
                sublayer = nn.Linear(
                    input_feature_size,
                    cur_expert_num, # t * p + s
                    weight_attr = nn.initializer.Constant(value = 0.1),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                )
            )
            self._param_gate_shared = linear
    
    def forward(self, input_data):
        # 输入为input_ple = [input_data] * (task_num + 1), 分别用户私有专家网络和共享专家网络的输入
        expert_outputs = []
        # 私有专家网络
        for i in range(0, self.task_num):
            for j in range(0, self.exp_per_task):
                linear_out = self._param_expert[i * self.task_num + j](input_data[i])
                expert_output = F.relu(linear_out)
                expert_outputs.append(expert_output) # T * p个[B, E]
        # 共享专家网络
        for i in range(0, self.shared_num):
            linear_out = self._param_expert[self.exp_per_task * self.task_num + i](input_data[-1])
            expert_output = F.relu(linear_out)
            expert_outputs.append(expert_output) # s个[B, E]

        # 任务门
        outputs = []
        for i in range(0, self.task_num):
            cur_expert_num = self.exp_per_task + self.shared_num
            linear_out = self._param_gate[i](input_data[i]) # 输入: 第一层[B, F],后续层[B, E], 输出:[B, p + s]
            cur_gate = F.softmax(linear_out, axis = 1) # [B, p + s]
            cur_gate = paddle.reshape(cur_gate, shape = [-1, cur_expert_num, 1]) # [B, p+s, 1]
            
            cur_experts = expert_outputs[i * self.exp_per_task:(i + 1) * self.exp_per_task] + expert_outputs[-int(self.shared_num):]
            expert_concat = paddle.concat(cur_experts, axis = 1) # [B, p+s, E]
            expert_concat = paddle.reshape(
                expert_concat, shape = [-1, cur_expert_num, self.expert_size] # [B, p+s, E]
            )
            cur_gate_expert = paddle.multiply(expert_concat, cur_gate) # [B, p+s, E]
            cur_gate_expert = paddle.sum(cur_gate_expert, axis = 1) # [B, E]
            outputs.append(cur_gate_expert) # 列表,T个[B, E]
        
        # 共享门, 不是最后一层才有
        if not self.if_last:
            cur_expert_num = self.task_num * self.exp_per_task + self.share_num # T*p + s
            linear_out = self._param_gate_shared(input_data[-1]) # 输入:[B,E],输出:[B, T*p+s]
            cur_gate = F.softmax(linear_out, axis = 1)
            cur_gate = paddle.reshape(cur_gate, shape = [-1, cur_expert_num, 1]) # [B, T*p+s, 1]
            cur_experts = expert_outputs
            expert_concat = paddle.concat(cur_experts, axis = 1)
            expert_concat = paddle.reshape(
                expert_concat, shape = [-1, cur_expert_num, self.expert_size] # [B, T*p+s, E]
            )
            cur_gate_expert = paddle.multiply(expert_concat, cur_gate) # [B, T*p+s, E]
            cur_gate_expert = paddle.sum(cur_gate_expert, axis = 1) # [B, E]
            outputs.append(cur_gate_expert) 
        
        return outputs # 列表,非最后一层: T + 1个[B, E], 最后一层: T个[B, E]


                
