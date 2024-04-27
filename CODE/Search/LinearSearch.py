def LinearSearch(arr,target):
    for elem in arr:
        if(elem==target):
            print("Target Found")
        else:
            print("Target Not Found")

arr=[1,2,3,4,5,6]
target=5
LinearSearch(arr,target)
