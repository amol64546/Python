# n = int(input())
# list = []
# for i in range(n):
#     ele = int(input())
#     list.append(ele)

list = [5,3,6,3,4,1,3]
n = len(list)

def bubble_sort(arr):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def selection_sort(arr):
    for i in range(n-1):
        minIdx = i
        for j in range(i+1,n):
            if arr[j]<arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[i],arr[minIdx] = arr[minIdx],arr[i]

def insertion_sort(arr):
    for i in range(1,n):
        curr = arr[i]
        j = i
        while j>0 and curr<arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = curr
        

# bubble_sort(list)
# selection_sort(list)
insertion_sort(list)
print(list)

