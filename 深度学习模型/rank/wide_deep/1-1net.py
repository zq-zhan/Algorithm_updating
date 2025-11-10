import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class WideDeepLayer(nn.Layer):
    def __init__(self, sparse_feature_number, sparse_feature_dim, dense_feature_dim, num_field, layer_sizes):
        super(WideDeepLayer, self).__init__()
        self.sparse_feature_number = sparse_feature_number
        self.sparse_feature_dim = sparse_feature_dim
        self.dense_feature_dim = dense_feature_dim
        self.num_field = num_field
        self.layer_sizes = layer_sizes

        self.wide_part = paddle.nn.Linear(
            in_features = self.dense_feature_dim,
            out_features = 1,
            weight_attr = paddle.ParamAttr(
                initializer = paddle.nn.initializer.TruncatedNormal(
                    mean = 0.0, std = 1.0 / math.sqrt(self.dense_feature_dim)
                ) # 截断正态分布初始化权重
            )
        )

        use_sparse = True
        if paddle.is_compiled_with_npu():
            use_sparse = False
        self.embedding = paddle.nn.Embedding(
            self.sparse_feature_number,
            self.sparse_feature_dim,
            sparse = use_sparse,
            weight_attr = paddle.ParamAttr(
                name = "SparseFeatFactors",
                initializer = paddle.nn.initializer.Uniform()
            )
        )

        sizes = [sparse_feature_dim * num_field + dense_feature_dim] + self.layer_sizes + [1]
        acts = ["relu" for _ in range(len(self.layer_sizes))] + [None]
        self._mlp_layers = []
        for i in range(len(layer_sizes) + 1):
            linear = paddle.nn.Linear(
                in_features = sizes[i],
                out_features = sizes[i + 1],
                weight_attr = paddle.ParamAttr(
                    initializer = paddle.nn.initializer.Normal(
                        std = 1.0 / math.sqrt(sizes[i])
                    )
                )
            )
            self.add_sublayer('linear_%d' % i, linear)
            self._mlp_layers.append(linear)
            if acts[i] == 'relu':
                act = paddle.nn.ReLU()
                self.add_sublayer('act_%d' % i, act)
                self._mlp_layers.append(act)

    def forward(self, sparse_inputs, dense_inputs):
        wide_output = self.wide_part(dense_inputs)

        sparse_embs = []
        for s_input in sparse_inputs:
            emb = self.embedding(s_input) # [batch_size, 1, sparse_feature_dim]
            emb = paddle.reshape(emb, shape = [-1, self.sparse_feature_dim]) # [batch_size, sparse_feature_dim]
            sparse_embs.append(emb)
        
        deep_output = paddle.concat(sparse_embs + [dense_inputs], concat = 1) # [batch_size, num_field * sparse_feature_dim + dense_feature_dim]
        for n_layer in self._mlp_layers:
            deep_output = n_layer(deep_output)
        
        prediction = paddle.add(wide_output, deep_output)
        pred = F.sigmoid(prediction)
        return pred