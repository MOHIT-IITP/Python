# sorting usign quick sort in python 
# i have also uploaded quick sort with cpp 
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:                      # only changed this part to convert this code to descending one 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quicksort(arr, start, pivot - 1)
        quicksort(arr, pivot + 1, end)

arr = [5, 4, 3, 3, 1, 77]
size=(len(arr)-1)
quicksort(arr, 0,size)
print("Sorted array:", arr)
