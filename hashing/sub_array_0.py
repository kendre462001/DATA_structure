arr=[4,-2,-1]
d=set()
total=0
for i,ele in enumerate(arr):
    total+=ele
    if total==0 or total in d :
        print('yes')
    d.add(total)
    # print(d)
print("no")