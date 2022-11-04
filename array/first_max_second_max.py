a=list(map(int,input().split()))
i=a[0]
j=a[1]

for ele in a:
    if ele>i :
        i=ele
    elif j<ele and j!=i:
        j=ele
print(i,j)