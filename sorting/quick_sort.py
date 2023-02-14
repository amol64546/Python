list = [5,3,6,3,4,1,3]
n = len(list)

def partition1(arr,l,r):
    pivot = arr[r]
    i = l
    for j in range(l,r+1):
        if pivot>=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    return i-1

def partition2(arr,l,r):
    pivot = arr[l]
    i = r
    for j in range(r,l-1,-1):
        if pivot<=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            i-=1
    return i+1

def partition3(arr,l,r):
    pivot = arr[(l+r)//2]
    i = l
    j = r
    while i<=j:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<=j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
    return i-1


def quick_sort(arr,l,r):
    if l>=r:
        return
    pi = partition1(arr,l,r)
    quick_sort(arr,l,pi-1)
    quick_sort(arr,pi+1,r)

quick_sort(list,0,len(list)-1)
print(list)
