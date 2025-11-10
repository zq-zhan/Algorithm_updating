import torch
import torch.nn as nn

class MultiFieldEmbedding(nn.Module):
    def __init__(self, field_cardinalities, embed_dims, share_fields = None):
        """
        field_cardinalities: dict
            每个变量的类别数，例如 {"city": 300, "province": 30, "country": 200}
        embed_dims: dict
            每个变量的embedding维度，例如 {"city": 8, "province": 8, "country": 8}
        share_fields: list
            想要共享embedding的变量名，例如 ["city", "province", "country"]。
            如果 None，则每个变量独立。
        """
        super(MultiFieldEmbedding, self).__init__()

        self.field_cardinalities = field_cardinalities
        self.embed_dims = embed_dims
        self.share_fields = share_fields

        self.embeddings = nn.ModuleDict()

        if share_fields is None:
            # 情况1:每个变量独立，即每个变量有专属的embedding
            for field, cardinality in field_cardinalities.items():
                self.embedddings[field] = nn.Embedding(
                    num_embdddings = cardinality,
                    embedding_dim = embed_dims[field]
                )
        else:
            # 情况2:多个变量共用一个embedding矩阵
            total_cardinality = sum(field_cardinalities[f] for f in share_fields)
            shared_dim = embed_dims[share_fields[0]]  # 假设共享维度一致
            self.embeddings['shared'] == nn.Embedding(
                num_embeddings = total_cardinality,
                embedding_dim = shared_dim
            )

            self.offsets = {}  # 记录每个field的偏移量，给不同变量的索引分配不重叠的编号区间，保证共享embedding查表时不混淆
            offset = 0
            for field in share_fields:
                self.offset[field] = offset
                offset += field_cardinalities[field]
    
    def forward(self, inputs):
        """
        inputs: dict
            {"city": Tensor(batch,), "province": Tensor(batch,), "country": Tensor(batch,)}
        """
        outputs = {}

        if self.share_fields is None:
            for field, x in inputs.items():
                outputs[field] = self.embeddings[field](x)
        else:
            for field, x in inputs.items():
                if field in self.share_fields:
                    offset_x = x + self.offsets[field]  # 偏移量
                    outputs[field] = self.embeddings['shared'](offset_x)
                else:
                    outputs[field] = self.embeddings[field](x)

        return outputs
