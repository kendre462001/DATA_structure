def findZeroes(arr, n, m) :
    # code here
    start=0
    end=0
    result=0
    count=0
    while end<n:
        if arr[end]==0:
            count+=1
            end+=1
        elif count<m:
            end+=1
        elif count>m:
            while count>m:
                if arr[start]==0:
                    count-=1
                start+=1
        else:
            if count==m:
                result=max(result,end-start+1)
                end+=1
    return result
n=11
arr=[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
m=2
print(findZeroes(arr,n,m))