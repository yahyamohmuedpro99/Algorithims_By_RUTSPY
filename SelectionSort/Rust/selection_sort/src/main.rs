fn smallest_index(arr: &Vec<i32>) -> usize {
    let mut smallest_element = arr[0];
    let mut smallest_index = 0;
    for i in 1..arr.len() {
       
        if arr[i] < smallest_element {
            smallest_element = arr[i];
            smallest_index = i;
        }
    }
    return smallest_index
}

fn selection_sort(arr:&Vec<i32>)->Vec<i32>{

    let mut copy_arr=arr.clone();
    let mut sorted_arr=Vec::new();
    for i in 0..arr.len(){
        let smallest_index=smallest_index(&copy_arr);
        sorted_arr.push(copy_arr.remove(smallest_index))


    }
    return sorted_arr;
}
fn main() {
    // drive
    let arr = vec![10, 3, 5, 7, 9, 11, 13];
    println!("{:?}", selection_sort(&arr));

}
