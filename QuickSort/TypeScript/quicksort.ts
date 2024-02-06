function quicksort(arr: number[]): number[] {
  if (arr.length < 2) {
    return arr;
  }
  let pivot=arr[0];
  let less=arr.filter((i)=>{return i<pivot})
  let greater=arr.filter((i)=>{return i>pivot})
  return quicksort(less).concat([pivot], quicksort(greater));
}
let l=[5,68,58,9,2,4]
console.log(quicksort(l))