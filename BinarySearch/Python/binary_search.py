
def binary_search(arr,target):
    low = 0
    high=len(arr)-1

    while low<=high:
        mid=int((low+high)/2)
        #found it in the mid
        if (target == arr[mid]):
            print(f'found {target} in index {mid}')
            return mid
        #if the target bigger than the middel so we need to search in bigger than mid
        elif(target>arr[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1

#driver
arr1 = [1, 3, 5, 7, 9, 11, 13]
target1 = 5
binary_search(arr1,target1)