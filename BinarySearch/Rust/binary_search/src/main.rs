fn binary_search(arr: &Vec<i32>, target: i32) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len() as i32 - 1;

    while low <= high {
        let mid = ((low + high) / 2) as usize;

        // found it in the mid
        if target == arr[mid] {
            println!("the {} is found at index {}", target, mid);
            return Some(mid);
        }
        // if the target is bigger than the mid, move cursor to after mid
        else if target > arr[mid] {
            low = mid as i32 + 1;
        }
        // if the target is lower than mid, move cursor of high down
        else {
            high = mid as i32 - 1;
        }
    }
    // If the target is not found, return None
    None
}

fn main() {
    // drive
    let arr = vec![1, 3, 5, 7, 9, 11, 13];
    let target = 5;
    binary_search(&arr, target);
}
