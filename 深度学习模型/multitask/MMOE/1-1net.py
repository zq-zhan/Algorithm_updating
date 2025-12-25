import paddle
import paddle.nn as nn
import paddle.nn.functional as F

class MMoELayer(nn.Layer):
    def __init__(self, feature_size, expert_num, expert_size, tower_size, gate_num):
        """
            Args:
                feature_size: 输入特征的维度
                expert_num: 专家个数,M
                expert_size: 每个专家的输出维度E
                gate_num：门/任务数，T
                tower_size: tower隐层大小，H
        """
        super().__init__()

        self.expert_num = expert_num # 专家个数，M
        self.expert_size = expert_size # 每个专家的输出维度，E
        self.tower_size = tower_size # tower隐层大小，H
        self.gate_num = gate_num # 门/任务数，T

        self._param_expert = []
        expert_init = [pow(10, -i) for i in range(1, self.expert_num + 1)] # 每个专家线性层的权重用不同常数初始化（逐个减小）
        for i in range(0, self.expert_num): # expert_num个共享专家，每个把输入feature_size映射到expert_size
            linear = self.add_sublayer(
                name = 'expert_' + str(i),
                sublayer = nn.Layer(
                    feature_size,
                    expert_size,
                    weight_attr = nn.initializer.Constant(value = expert_init[i]),
                    bias_zttr = nn.initializer.Constant(value = 0.1),
                    name = 'expert_' + str(i)
                )
            ) # [B, E]
            self._param_expert.append(linear)
        
        self._param_gate = []
        self._param_tower = []
        self._param_tower_out = []
        gate_init = [pow(10, -i) for i in range(1, self.gate_num + 1)]
        for i in range(0, self.gate_num):
            linear = self.add_sublayer(
                name = 'gate_' + str(i),
                sublayer = nn.Linear(
                    feature_size,
                    expert_num,
                    weight_attr = nn.initializer.Constant(value = gate_init[i]),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = 'gate_' + str(i)
                )
            ) # [B, M]，转化为[B, M, 1]后与上面输出concat后的[B, M, E]相乘，得到混合加权后的专家表示
            self._param_gate.append(linear)

            linear = self.add_sublayer(
                name = 'tower_' + str(i),
                sublayer = nn.Linear(
                    expert_size,
                    tower_size,
                    weight_attr = nn.initializer.Constant(value = pow(10, -i)),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = 'tower_' + str(i)
                )
            ) # [B, H]
            self._param_tower.append(linear)

            linear = self.add_sublayer(
                name = 'tower_out_' + str(i),
                sublayer = nn.Linear(
                    tower_size,
                    2,
                    weight_attr = nn.initializer.Constant(value = pow(10, -i)),
                    bias_attr = nn.initializer.Constant(value = 0.1),
                    name = 'tower_out_' + str(i)
                )
            )
            self._param_tower_out.append(linear)
    
    def forward(self, input_data):
        expert_outputs = []
        for i in range(0, self.expert_num):
            linear_out = self._param_expert[i](input_data) # [B, E]
            expert_output = F.relu(linear_out)
            expert_outputs.append(expert_output)
        expert_concat = paddle.concat(expert_outputs, axis = 1) # [B, M * E]
        expert_concat = paddle.reshape(
            expert_concat, [-1, self.expert_num, self.expert_size]
        ) # [B, M, E]

        output_layers = []
        for i in range(0, self.gate_num):
            cur_gate_linear = self._param_gate[i](input_data) # [B, M]
            cur_gate = F.softmax(cur_gate_linear, axis = 1)
            cur_gate = paddle.reshape(cur_gate, [-1, self.expert_num, 1]) # [B, M, 1]
            cur_gate_expert = paddle.multiply(expert_concat, cur_gate) # [B, M, E]
            cur_gate_expert = paddle.sum(x = cur_gate_expert, axis = 1) # [B, E]
            cur_tower = self._param_tower[i](cur_gate_expert) # [B, H]
            cur_tower = F.relu(cur_tower)
            out = self._param_tower_out[i](cur_tower) # [B, 2]
            out = F.softmax(out, axis = 1)
            out = paddle.clip(out, min = 1e-5, max = 1.0 - 1e-5)
            output_layers.append(out) # 长度为gate_num的列表，每个元素是[B, 2]的概率向量，ctcvr多目标优化中gate_num = 2
        
        return output_layers
