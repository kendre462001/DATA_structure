a=[]
count=1

n=4
c=5
for i in range(n):
    a.append([ele for ele in range(count,count+c)])
    count+=c


start=0
end=c-1
bottom_l=n-1
bottom_r=0

while start<end and bottom_r<bottom_l:
    for i in range(start,end):
        print(a[start][i])
    
    for i in range(start,end):
        print(a[i][end])
    end-=1
    for i in range(end,-1,-1):
        print(a[bottom_l][i])
    
    for i in range(bottom_l-1,0,-1):
        print(a[i][start])
    bottom_r-=1
    # end-=1
    start+=1

    
