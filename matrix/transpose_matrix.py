list1=[]
n=int(input())
m=int(input())
for i in range(n):
    list1.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i+1,m):
        list1[i][j],list1[j][i]=list1[j][i],list1[i][j]
for ele in list1:
    print(*ele)
        
