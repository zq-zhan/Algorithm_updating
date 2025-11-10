import math
import paddle
from net import DNNLayer, StaticDNNLayer

class StaticModel():
    def __init__(self, config):
        self.cost = None
        self.infer_target_var = None
        self.config = config
        self.__init_hyper_parameters()
        self.sync_mode = config.get("runner.sync_mode")
    
    def _init_hyper_parameters(self):
        self.is_distributed = False
        self.distributed_embedding = False

        if self.config.get("hyper_parameters.distributed_embedding", 0) == 1:
            self.distributed_embedding = True
        
        self.sparse_feature_number = self.config.get(
            "hyper_parameters.sparse_feature_number"
        )
        self.sparse_feature_dim = self.config.get(
            "hyper_parameters.sparse_feature_dim"
        )
        self.sparse_input_slots = self.config.get(
            "hyper_parameters.sparse_input_slots"
        )
        self.dense_input_dim = self.config.get(
            "hyper_parameters.dense_input_dim"
        )
        self.learning_rate = self.config.get(
            "hyper_parameters.learning_rate"
        )
        self.fc_sizes = self.config.get("hyper_parameters.fc_sizes")

    def create_feeds(self, is_infer = False):
        dense_input = paddle.static.data(
            name = "dense_input",
            shape = [None, self.dense_input_dim],
            dtype = "float32"
        ) # 静态图里定义输入张量的占位符

        sparse_input_ids = [
            paddle.static.data(
                name = "C" + str(i), shape=[None, 1], dtype = "int64"
            ) for i in range(1, self.sparse_input_slots)
        ]

        label = paddle.static.data(
            name = "label", shape = [None, 1], dtype = "int64"
        )
        feeds_list = [label] + sparse_input_ids + [dense_input]
        return feeds_list
    
    def net(self, input, is_infer = False):
        self.label_input = input[0]
        self.sparse_input = input[1:self.sparse_input_slots]
        self.dense_input = input[-1]

        sparse_number = self.sparse_input_slots - 1

        dnn_model = DNNLayer(
            self.sparse_feature_number,  # 词汇表大小
            self.sparse_feature_dim,
            self.dense_input_dim,
            sparse_number,
            self.fc_sizes,
            sync_mode = self.sync_mode
        )

        raw_predict_2d = dnn_model(self.sparse_input, self.dense_input)

        predic_2d = paddle.nn.functional.softmax(raw_predict_2d)  # 二维输出映射为二维概率

        self.predict = predic_2d

        auc, batch_auc, _ = paddle.static.auc(
            input = self.predict,
            label = self.label_input,
            num_thresholds = 2 ** 12,
            slide_steps = 20
        )
        self.inference_target_var = auc
        if is_infer:
            fetch_dict = {'auc':auc}
            return fetch_dict

        cost = paddle.nn.functional.cross_entropy(
            input = raw_predict_2d, label = self.label_input
        )
        avg_cost = paddle.mean(x = cost)
        self._cost = avg_cost

        fetch_dict = {'cost':avg_cost, 'auc':auc}
        return fetch_dict
    
    def create_optimizer(self, strategy = None):
        optimizer = paddle.optimizer.Adam(
            learning_rate = self.learning_rate,
            lazy_mode = True
        ) # lazy_mode=True = 只更新 sparse embedding 有梯度的行，提高稀疏训练效率
        if strategy != None:
            import paddle.distributed.fleet as fleet
            optimizer = fleet.distributed_optimizer(optimizer, strategy)
        optimizer.minimize(self._cost)
    
    def infer_net(self, input):
        return self.net(input, is_infer=True)
