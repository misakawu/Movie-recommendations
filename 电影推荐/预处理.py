user_points={}#user:points[a,b,c,...]
points=[]
all=[]
with open('u.data', 'r') as f:
    for line in f.readlines():
        user_id,movie_id,point,time=line.split('	')
        user_id=int(user_id)
        movie_id=int(movie_id)
        point=int(point)
        all.append([user_id,movie_id,point])
        
    for date in all:
        user=date[0]
        id=date[1]
        p=date[2]
        
        if user not in user_points:
            user_points[user]=[]
            for i in range(1683):
                user_points[user].append(0)
            user_points[user][id]=p
        else:
            user_points[user][id]=p
user_points=sorted(user_points.items(),key=lambda d:d[0],reverse=False)
#所有人对每个电影的评分
with open('user_points.data', 'w') as f:
    for i in user_points:
        f.write(str(i[0])+'    ')
        for j in i[1]:
            f.write(str(j)+'|')  
        f.write('\n')
    
        
        
        
        
        
        
        
        
        
        