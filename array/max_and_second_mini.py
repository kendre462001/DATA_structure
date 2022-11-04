arr=list(map(int,input().split()))

i=arr[0]
j=arr[0]
pre=float("inf")

for ele in arr:
    if i<ele:
        i=ele
    if ele<j:
        j=ele
    elif ele!=j:
        if ele<pre:
            pre=ele

print(i,pre)
