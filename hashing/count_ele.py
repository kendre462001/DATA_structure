
arr=[1,2,3,4,5,2,3,4,1,1,1,1,5,6]
target=2
d={}
for ele in arr:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
print(d.get(target,"-1"))
