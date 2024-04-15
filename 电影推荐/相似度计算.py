#pearson系数版
import math
points=[]
with open('user_points.data', 'r') as f:
    for line in f.readlines():
        user,point=line.split('   ')
        point=list(point.split('|'))
        point.pop()
        new_p=[]
        for i in point:
            new_p.append(int(i))
        points.append(new_p)
#print(points)

users_similarity=[]#[[s00,s01,..],[s10,s11],..]

for i,x in enumerate(points):
    users_similarity.append([])
    print(i/1000)
    for j,y in enumerate(points):
        if x==y:
            users_similarity[i].append(1)
        else:
            XY=0
            X=0
            Y=0
            X2=0
            Y2=0
            l=len(x)
            for num in range(l):
                XY+=x[num]*y[num]
                X+=x[num]
                Y+=y[num]
                X2+=x[num]*x[num]
                Y2+=y[num]*y[num]
            den=math.sqrt( (X2-X*X/l) * (Y2-Y*Y/l) )
            mol=XY-X*Y/l
            P=mol / den
            users_similarity[i].append(P)
#print(users_similarity)

print('开始写入')
with open('users_similarity.data', 'w') as f:
    for user in users_similarity:
        for i in user:
            f.write(str(i)+'|')
        f.write('\n')
    
    
    
    
    