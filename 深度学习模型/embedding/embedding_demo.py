# 连续行特征离散化 + 离散特征 --> embedding --> 归一化

## 离散特征
user_emb = user_embedding(user_id)
city_emb = city_embedding(city) # 要在同一映射空间内进行embedding

## 连续特征
x = paddle.log1p(paddle.clip(click_cnt, max = 10000))
bucket_id = paddle.bucketsize(x, boundaries)
cnt_emb = cnt_embedding(bucket_id) # 要在同一映射空间内进行embedding

## 序列特征（DIEN逻辑）
seq_emb = paddle.mean(item_embs * time_decay, axis = 1)

## 融合
all_embs = paddle.concat(
    [user_emb, city_emb, cnt_emb, seq_emb], axis = 1
)
all_embs = layer_norm(all_embs) # 归一化

final_emb = mlp(all_embs) # MLP层