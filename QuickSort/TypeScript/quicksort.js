function quicksort(arr) {
    if (arr.length < 2) {
        return arr;
    }
    var pivot = arr[0];
    var less = arr.filter(function (i) { return i < pivot; });
    var greater = arr.filter(function (i) { return i > pivot; });
    return quicksort(less).concat([pivot], quicksort(greater));
}
var l = [5, 68, 58, 9, 2, 4];
console.log(quicksort(l));
