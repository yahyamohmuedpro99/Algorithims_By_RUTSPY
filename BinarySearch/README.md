### Binary Search

Binary search is a fast and efficient algorithm used to find a target value within a sorted array or list. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty.

#### How it works:

1. **Initialize**: Start with the entire sorted array.

2. **Midpoint**: Compute the midpoint of the array.

3. **Comparison**: Compare the target value with the value at the midpoint.

4. **Update Interval**:
   - If the target value is equal to the midpoint value, the search is complete.
   - If the target value is less than the midpoint value, search the left half of the array.
   - If the target value is greater than the midpoint value, search the right half of the array.

5. **Repeat**: Continue the process recursively on the selected half until the target value is found or the interval is empty.

#### Key Points:

- Binary search works efficiently on sorted arrays.
- It has a time complexity of O(log n), making it much faster than linear search for large datasets.
- It can be implemented recursively or iteratively.

#### Example:

Let's search for the value `7` in the sorted array `[1, 3, 5, 7, 9, 11, 13]`.

1. Start with the entire array `[1, 3, 5, 7, 9, 11, 13]`.
2. Compute the midpoint (index 3) with value `7`.
3. The target value matches the midpoint value, so the search is complete.
4. The index of the target value (`7`) is returned as `3`.

Binary search efficiently locates the target value (`7`) in just a few steps.
