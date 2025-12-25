import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class ESMMLayer(nn.Layer):
    def __init__(self, sparse_feature_number, sparse_feature_dim, num_field,
                 ctr_layer_sizes, cvr_layer_sizes):
        super().__init__()
        self.sparse_feature_number = sparse_feature_number
        self.sparse_feature_dim = sparse_feature_dim
        self.num_field = num_field
        self.ctr_layer_sizes = ctr_layer_sizes
        self.cvr_layer_sizes = cvr_layer_sizes

        use_sparse = True
        if paddle.is_compiled_with_custom_device('npu'):
            use_sparse = False
        
        self.embedding = nn.Embedding(
            self.sparse_feature_number,
            self.sparse_feature_dim,
            sparse = use_sparse,
            padding_idx = 0,
            weight_attr = paddle.ParamAttr(
                name = "SparseFeatFactors",
                initializer = nn.initializer.Uniform()
            )
            )
        
        # ctr_part
        ctr_sizes = [sparse_feature_dim * num_field] + self.ctr_layer_sizes + [2]
        acts = ["relu" for _ in range(len(self.ctr_layer_sizes))] + [None]
        self._ctr_mlp_layers = []
        for i in range(len(ctr_layer_sizes) + 1):
            linear = paddle.nn.Linear(
                in_features = ctr_sizes[i],
                out_features = ctr_sizes[i + 1],
                weight_attr = paddle.ParamAttr(
                    initializer = nn.initializer.Normal(
                        std = 1.0 / math.sqrt(ctr_sizes[i])
                    )
                )
            )
            self.add_sublayer('linear_%d' % i, linear)
            self._ctr_mlp_layers.append(linear)
            if acts[i] == 'relu':
                act = paddle.nn.ReLU()
                self.add_sublayer('act_%d' % i, act)
                self._ctr_mlp_layers.append(act)
            
        # cvr_part
        cvr_sizes = [sparse_feature_dim * num_field] + self.cvr_layer_sizes + [2]
        acts = ["relu" for i in range(len(self.cvr_layer_sizes))] + [None]
        self._cvr_mlp_layers = []
        for i in range(len(self.cvr_layer_sizes) + 1):
            linear = paddle.nn.Linear(
                in_features = cvr_sizes[i],
                out_features = cvr_sizes[i + 1],
                weight_attr = paddle.ParamAttr(
                    initializer = nn.initializer.Normal(
                        std = 1.0 / math.sqrt(cvr_sizes[i])
                    )
                )
            )
            self.add_sublayer('linear_%d' % i, linear)
            self._cvr_mlp_layers.append(linear)
            if acts[i] == 'relu':
                act = paddle.nn.ReLU()
                self.add_sublayer('act_%d' % i, act)
                self._cvr_mlp_layers.append(act)

    def forward(self, inputs):
        # input:[B, F]，其中F为num_field，每个filed的数据为[B, K],K为该field的sparse特征的个数
        emb = []
        for data in inputs: 
            # 对每个field的sparse特征进行embedding
            # data: [B, K],K为max_len
            feat_emb = self.embedding(data) # [B, K, D],D为sparse_feature_dim
            feat_emb = paddle.sum(feat_emb, axis = 1) # [B, D]
            emb.append(feat_emb)
        concat_emb = paddle.concat(emb, axis = 1) # [B, F * D]

        ctr_output = concat_emb
        for n_layer in self._ctr_mlp_layers:
            ctr_output = n_layer(ctr_output)
        
        ctr_out = F.softmax(ctr_output)

        cvr_output = concat_emb
        for n_layer in self._cvr_mlp_layers:
            cvr_output = n_layer(cvr_output)
        
        cvr_out = F.softmax(cvr_output) # [B, 2]

        ctr_prop_one = paddle.slice(ctr_out, axes = [1], starts = [1], ends = [2]) # 正类概率,取第二列. [B, 1]
        cvr_prop_one = paddle.slice(cvr_out, axes = [1], starts = [1], ends = [2]) # 正类概率,取第二列
        ctcvr_prop_one = paddle.multiply(ctr_prop_one, cvr_prop_one) # 正类概率乘积
        
        ctcvr_prop = paddle.concat(
            x = [1-ctcvr_prop_one, ctcvr_prop_one], axis = 1
        )
        return ctr_out, ctr_prop_one, cvr_out, cvr_prop_one, ctcvr_prop, ctcvr_prop_one






        