arr=[4, 3, 5, 6]
x=12
d={}
flag=0
for i,ele in enumerate(arr):
    if d.get(x-ele)==None:
        d[ele]=i
    elif d.get(x-ele)!=None:
        print("yes")
        flag=1
        break
if not flag:
    print("NO")
