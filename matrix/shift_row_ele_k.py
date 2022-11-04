n,m,k=map(int,input().split())
mat=[]

for i in range(n):
    mat.append(list(map(int,input().split())))

for ele in mat:
    print(*ele[k:]+ele[:k])