/**
 * performs a binary search on the given sorted array to find the target element.
 * @param arr The sorted array to search in.
 * @param target The target element to search for.
 * @returns The index of the target element if found, otherwise returns "not exists".
 */
function BinarySearch(arr: Array<number>, target: number): number {
  let low = 0; 
  let high = arr.length - 1;

  // Loop until the low index is less than or equal to the high index.
  while (low <= high) {
    let mid = (low + high) / 2;

    // if target found at the middle index, return the index.
    if (target === arr[mid]) {
      console.log(
        "the target element is " + target + " and it located at index: " + mid
      );
      return mid;
    } 
    // If the target is greater than the element at the middle index,
    // adjust the low index to search in the right half of the array.
    else if (target > arr[mid]) {
      low = mid + 1;
    } 
    // If the target is less than the element at the middle index,
    // adjust the high index to search in the left half of the array.
    else {
      high = mid - 1;
    }
  }

  // If the target element is not found log "not exists".
  console.log("not exist")
  return -1
}


// driver

// if it exist
// let arr1 = [1, 3, 5, 7, 9, 11, 13];
// let target1 = 5;
// BinarySearch(arr1, target1);

// if its not exist
// let arr = [1, 3, 5, 7, 9, 11, 13];
// let target = 55;
// BinarySearch(arr, target);
