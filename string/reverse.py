n=int(input())
t=0
while n>3:
    if n%2==0:
        n=n//2
        t+=1
    else:
        for i in range(n-1,0,-2):
            if n%i==0:
                n=n//i
                t+=1
                break
print(t)
    