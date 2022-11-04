arr=[1,1,2,2,3,3,4,4,5,6,7,5,6,7]
d={}
for ele in arr:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
flag=0
for ele,value in d.items():
    if value==1:
        print(ele,end=" ")
        flag=1
if not flag:
    print("no unique ele in arr")
