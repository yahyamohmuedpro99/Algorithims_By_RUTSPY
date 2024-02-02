function smallest_index(arr) {
    var smallest_element = arr[0];
    var smallest_index = 0;
    // Find the index of the smallest element in the array
    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < smallest_element) {
            smallest_element = arr[i];
            smallest_index = i;
        }
    }
    return smallest_index;
}
function selection_sort(arr) {
    var copy_arr = arr.slice();
    var sorted_arr = [];
    for (var i = 0; i < arr.length; i++) {
        var smallest_idx = smallest_index(copy_arr);
        sorted_arr.push(copy_arr.splice(smallest_idx, 1)[0]);
    }
    console.log(sorted_arr);
    return sorted_arr;
}
var arr = [555, 69, 9];
console.log(selection_sort(arr));
