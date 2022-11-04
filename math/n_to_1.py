
n=int(input())

count=0

while n>1:

    if n%3==0:
        n=n//3
    elif n%3==1:
        n-=1
    else:
        if n==2:
            n-=1
        else:
            n+=1
    count+=1
print(count)