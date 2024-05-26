# This program check if the array is sorted or not
def checkSort(arr,szz):
    if szz==0 or szz==1:
        return True
    return (arr[szz-1]>=arr[szz-2] and checkSort(arr,szz-1))

arr=[1,2,6,23]
szz=len(arr)
checkSort(arr,szz)
if checkSort(arr,szz):
    print("yes")
else:
    print("no")


