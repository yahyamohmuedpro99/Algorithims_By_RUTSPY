fn quick_sort(arr: Vec<usize>) -> Vec<usize> {
    if arr.len() < 2 {
        return arr;
    }
    let pivot = arr[1];
    let less: Vec<usize> = arr.iter().copied().filter(|&x| x < pivot).collect();
    let greater: Vec<usize> = arr.iter().copied().filter(|&x| x > pivot).collect();
    let mut sorted = quick_sort(less);
    sorted.push(pivot);
    sorted.extend(quick_sort(greater));
    println!("{:?}", &sorted);
    sorted
}

fn main() {
    let arr: Vec<usize> = vec![ 3, 4,8, 5];
    println!("{:?}", quick_sort(arr));
}
