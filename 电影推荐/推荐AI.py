user_similarity=[]

print('读取文件')
points=[]#二维储存所有人对所有电影的评分
with open('user_points.data', 'r') as f:
    for i,line in enumerate(f.readlines()):
        user,point=line.split('   ')
        point=list(point.split('|'))
        point.pop()
        new_p=[]
        for i in point:
            new_p.append(int(i))
        points.append(new_p)

movie_recom_point=[]
with open('users_similarity.data', 'r') as f:
    for i,line in enumerate(f.readlines()):
        x=list(line.split('|'))
        x.pop()
        new_x=[]#第i人与其他人的相似度
        for j in x:
            new_x.append(float(j))
            
        tem=[]#第i人的推荐指数
        for poi in range(len(points[0])):
            tem.append(0)
        for x,er in enumerate(new_x):
            for y,upoint in enumerate(points[x]):
                recpoint=er*upoint
                tem[y]+=recpoint
        tem.pop(0)
        movie_recom_point.append(tem)

print('开始写入')
w=open('movie_recom_point.data','w')
for i,one_user_point in enumerate(movie_recom_point):
    w.write(str(i+1)+'    ')
    for point in one_user_point:
        point=round(point,1)
        w.write(str(point)+'|')
    w.write('\n')
        
        
