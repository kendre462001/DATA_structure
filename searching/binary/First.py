arr=[1,2,3,4,5,6,6,7,7,8,9,10]
n=len(arr)
start=0
end=n-1
target=6
def binary_first(arr,n,start,end,target):
    while start<end:
        mid=(start+end)//2
        if target==arr[mid]:
            if arr[mid-1]==target:
                end-=1
            else:

                # return arr[mid],mid
                return mid
        elif arr[mid]>target:
            end-=1
        elif arr[mid]<target:
            start+=1
    return -1
(binary_first(arr,n,start,end,target))