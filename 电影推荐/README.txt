movie_recom_point.data 为最终计算结果，内容为每个人对所有电影的推荐指数 格式：id	指数1|指数2|.....

user_points.data 为每个人对所有电影的评分 格式：id	0|评分1|评分2|......

users_similarity.data 为所有人之间评分的相似度 格式：与user1的相似度|与user2的相似度|....
			（与自己的相似度为1）

u.data和u.item为元数据包

预处理.py 调用u.data和u.item计算user_points.data 

相似度计算.py 调用user_points.data计算users_similarity.data

推荐AI.py 调用user_points.data 和users_similarity.data计算movie_recom_point.data 

（使用欧式距离法+“人以群分”模式）