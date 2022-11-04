list1=[]

n=int(input())
count=1
for i in range(n):
    list1.append([ele for ele in range(count,count+3)])
    count+=3

for i in range(n):
    for j in range(i+1,n):
        list1[i][j],list1[j][i]=list1[j][i],list1[i][j]


start=0
end=n-1
while start<end:
    list1[start],list1[end]=list1[end],list1[start]
    start+=1
    end-=1
print(*list1)