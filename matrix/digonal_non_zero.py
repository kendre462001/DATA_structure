# from selectors import EpollSelector


list1=[]
n=int(input())

for i in range(n):
    for j in range(n):
        list1.append(list(map(int,input().split())))
def check(list1,n):
    for i in range(n):
        # flag=False
        for j in range(n):
            if i==j:
                if list1[i][j]==0:
                    return 0
                else:
                    continue

            elif j==n-i-1:
                if list1[i][j]==0:
                    return 0
                else:
                    continue
            else:
                if list1[i][j]!=0:
                    return 0
                else:
                    continue
                
    return 1
print(check(list1 , n))
