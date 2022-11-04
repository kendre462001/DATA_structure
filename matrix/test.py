
arr1=list(map(int,input().split()))
arr2=list(map(str,input().split()))
temp=[]
i=0
j=0
while i<len(arr1):
    temp.append(arr1[i])
    i+=1
    if j<len(arr2):
        temp.append(arr2[j])
        j+=1
print(temp)
