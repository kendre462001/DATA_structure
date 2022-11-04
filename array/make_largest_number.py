n=int(input())
arr=list(map(int,input().split()))

# string campare algorithm

res=""

for i in range(n):
    for j in range(i+1,n):
        if arr[j]!="*":
            res=res+check()