list = [5,3,6,3,4,1,3]
n = len(list)

def merge(arr,l,m,r):
    temp = [0] * (r-l+1)
    k = 0
    i=l
    j=m+1
    while i<=m and j<=r:
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1
    
    while i<=m:        
        temp[k] = arr[i]        
        k+=1; i+=1

    while j<=r:        
        temp[k] = arr[j]
        k+=1; j+=1
    
    k=0
    for i in range(l,r+1):
        arr[i] = temp[k]
        k+=1



def merge_sort(arr,l,r):
    if l>=r:
        return
    mid = (l+r)//2
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    merge(arr,l,mid,r)

merge_sort(list,0,len(list)-1)
print(list)


