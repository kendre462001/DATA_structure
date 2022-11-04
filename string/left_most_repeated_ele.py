s=input()
d={}

for ele in s:
    if ele in d:
        d[ele]+=1
    else:
        d[ele]=1
print(d)
i=0
for index,ele in enumerate(s):
    # if d.get(ele)!=None:
    if d[ele]>1:
        print(i)
        break
    i+=1