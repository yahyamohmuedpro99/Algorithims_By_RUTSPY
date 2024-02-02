"""
------ Selection Sort --------
in this we try to sort the array by select the smallest element
and put in new array and reapeat the same for all the array and compare 
the Big(O) is O(n^2)

==> how the approach works
    - first make function get me smallest index in array
    - use this to take the smallest element and put it in new array
"""
def smallest_index(arr):
    smallest_element = arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest_element:
            smallest_element = arr[i]
            smallest_index=i
    return smallest_index

def selection_sort(arr):
    #to make the original arr not changed 
    copy_list=arr.copy()
    sorted_arr = []
    for i in range(len(copy_list)):
        smallest_idx = smallest_index(copy_list)
        sorted_arr.append(copy_list.pop(smallest_idx))
    return sorted_arr

arr=[5,69,35,68,6,30,4]
sorted_arr=selection_sort(arr)

print(f"Original : {arr} \nSorted : {sorted_arr}")