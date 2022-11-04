from First import binary_first
arr=[1,2,3,4,5,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,9,10]
n=len(arr)
start=0
end=n-1
target=10
def binary_last(arr,n,start,end,target):
    while start<end:
        mid=(start+end)//2
        if target==arr[mid]:
            if arr[mid+1]<=target:
                start+=1
            else:

                # return arr[mid],mid
                return mid
        elif arr[mid]>target:
            end-=1
        elif arr[mid]<target:
            start+=1
    return -1
print(binary_last(arr,n,start,end,target))
# below print statement useful for getting target which are present front as well as last 
print(binary_first(arr,n,start,end,target),binary_last(arr,n,start,end,target))

#count of a target 
print(binary_last(arr,n,start,end,target)-binary_first(arr,n,start,end,target)+1)