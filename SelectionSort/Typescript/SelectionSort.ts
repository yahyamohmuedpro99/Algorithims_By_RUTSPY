function smallest_index(arr: number[]): number {
    let smallest_element = arr[0];
    let smallest_index = 0;
  
    // Find the index of the smallest element in the array
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] < smallest_element) {
        smallest_element = arr[i];
        smallest_index = i;
      }
    }
  
    return smallest_index;
  }
  
  function selection_sort(arr: number[]): number[] {
    let copy_arr=arr.slice();
    let sorted_arr: number[] = [];
    for (let i = 0; i < arr.length; i++) {
      let smallest_idx = smallest_index(copy_arr);
      sorted_arr.push(copy_arr.splice(smallest_idx,1)[0]); 
    }
  
    console.log(sorted_arr);
    return sorted_arr;
  }
  
  let arr = [555, 69,9];
  console.log(selection_sort(arr));
  