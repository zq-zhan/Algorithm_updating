import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class StaticDNNLayer(nn.Module):
    def __init__(self, sparse_feature_number, sparse_feature_dim,
                 dense_feature_dim, num_field, layer_sizes):
        super(StaticDNNLayer, self).__init__()
        self.sparse_feature_number = sparse_feature_number
        self.sparse_feature_dim = sparse_feature_dim
        self.dense_feature_dim = dense_feature_dim
        self.num_field = num_field
        self.layer_sizes = layer_sizes # mlp隐藏层维度

        self.embedding = paddle.nn.Embedding(
            self.sparse_feature_number,
            self.sparse_feature_dim,
            sparse = True,
            weight_attr = paddle.ParamAttr(
                name = "SparseFeatFactors",
                initializer = paddle.nn.initializer.Uniform()
            ))
        
        sizes = [sparse_feature_dim * num_field + dense_feature_dim
                 ] + self.layer_sizes + [2] # 输入特征总维度+隐藏层维度+输出层维度(二分类)
        acts = ["relu" for _ in range(len(self,layer_sizes))] + [None]
        self._mlp_layers = []
        for i in range(len(layer_sizes) + 1):
            linear = paddle.nn.Linear(
                in_features = sizes[i],
                out_features = sizes[i + 1],
                weight_attr = paddle.ParamAttr(
                    initializer = paddle.nn.initializer.Normal(
                        std = 1.0/math.sqrt(sizes[i])
                    )
                )
            )
            self.add_sublayer('linear_%d' % i, linear) # 动态添加网络层
            self._mlp_layers.append(linear)
            if acts[i] == 'relu':
                act = paddle.nn.ReLU()
                self.add_sublayers('act_%d' % i, act)
                self._mlp_layers.append(act)

    def forward(self, sparse_inputs, dense_inputs):
        '''
            sparse_input: [batch_size, num_field], list，长度为num_field，如27
            dense_input: [batch_size, dense_feature_dim]
        '''
        sparse_embs = []
        for s_input in sparse_inputs:  # s_input代表该field对应的特征id,[batch_size, 1]
            if self.sync_mode == "gpubox":
                emb = paddle.fluid.contrib.sparse_embedding(
                    input = s_input,
                    size = [
                        self.sparse_feature_number, self.sparse_feature_dim
                    ],
                    param_attr = paddle.ParamAtrr(name = "embedding")
                )
            else:
                emb = self.embedding(s_input)  # 输出[batch_size, 1, sparse_feature_dim]
            emb = paddle.reshape(emb, shape = [-1, self.sparse_feature_dim]) # 输出[batch_size, sparse_feature_dim]，flatten 成一个特征向量
            sparse_embs.append(emb)
            
        y_dnn = paddle.concat(x = sparse_embs + [dense_inputs], axis = 1) # [batch_size, num_field * sparse_feature_dim + dense_feature_dim]，因为spares_embs中的各个num_field的embedding向量横向拼接
        for n_layer in self._mlp_layers:
            y_dnn = n_layer(y_dnn)
        return y_dnn
    


class StaticDNNLayer(nn.Module):
    def __init__(self, sparse_feature_number, sparse_feature_dim,
                 dense_feature_dim, num_field, layer_sizes):
        super(StaticDNNLayer, self).__init__()
        self.sparse_feature_number = sparse_feature_number
        self.sparse_feature_dim = sparse_feature_dim
        self.dense_feature_dim = dense_feature_dim
        self.num_field = num_field
        self.layer_sizes = layer_sizes # mlp隐藏层维度

        # self.embedding = paddle.nn.Embedding(
        #     self.sparse_feature_number,
        #     self.sparse_feature_dim,
        #     sparse = True,
        #     weight_attr = paddle.ParamAttr(
        #         name = "SparseFeatFactors",
        #         initializer = paddle.nn.initializer.Uniform()
        #     ))
        
        sizes = [sparse_feature_dim * num_field + dense_feature_dim
                 ] + self.layer_sizes + [2] # 输入特征总维度+隐藏层维度+输出层维度(二分类)
        acts = ["relu" for _ in range(len(self,layer_sizes))] + [None]
        self._mlp_layers = []
        for i in range(len(layer_sizes) + 1):
            linear = paddle.nn.Linear(
                in_features = sizes[i],
                out_features = sizes[i + 1],
                weight_attr = paddle.ParamAttr(
                    initializer = paddle.nn.initializer.Normal(
                        std = 1.0/math.sqrt(sizes[i])
                    )
                )
            )
            self.add_sublayer('linear_%d' % i, linear) # 动态添加网络层
            self._mlp_layers.append(linear)
            if acts[i] == 'relu':
                act = paddle.nn.ReLU()
                self.add_sublayers('act_%d' % i, act)
                self._mlp_layers.append(act)

    def forward(self, sparse_embs, dense_inputs):
        # sparse_embs = []
        # for s_input in sparse_inputs:  # s_input代表该field对应的特征id,[batch_size, 1]
        #     if self.sync_mode == "gpubox":
        #         emb = paddle.fluid.contrib.sparse_embedding(
        #             input = s_input,
        #             size = [
        #                 self.sparse_feature_number, self.sparse_feature_dim
        #             ],
        #             param_attr = paddle.ParamAtrr(name = "embedding")
        #         )
        #     else:
        #         emb = self.embedding(s_input)  # 输出[batch_size, 1, sparse_feature_dim]
        #     emb = paddle.reshape(emb, shape = [-1, self.sparse_feature_dim]) # 输出[batch_size, sparse_feature_dim]，flatten 成一个特征向量
        #     sparse_embs.append(emb)
            
        y_dnn = paddle.concat(x = sparse_embs + [dense_inputs], axis = 1) # [batch_size, num_field * sparse_feature_dim + dense_feature_dim]，因为spares_embs中的各个num_field的embedding向量横向拼接
        for n_layer in self._mlp_layers:
            y_dnn = n_layer(y_dnn)
        return y_dnn