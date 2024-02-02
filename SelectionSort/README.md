# Selection Sort Algorithm

## Introduction
The Selection Sort algorithm is a straightforward sorting technique used to organize elements in an array in a specified order (ascending or descending). It works by repeatedly finding the smallest (or largest) element from the unsorted section of the array and moving it to the beginning (or end). This process is repeated for each position in the array.

## Complexity
The time complexity of Selection Sort is `O(n^2)`, where `n` is the number of elements in the array. This quadratic time complexity arises because the algorithm performs two nested loops over the array: one to iterate over each element and another to find the smallest (or largest) element.

## How the Approach Works
1. **Find the Smallest Element**: Implement a function to identify the smallest element in the array. This function scans the array and keeps track of the index of the smallest element found.

2. **Sort the Array**: Use the function to select the smallest element from the unsorted portion of the array. Remove this element from the original array and append it to a new array. This step is repeated until all elements have been removed from the original array and inserted into the new array in sorted order.

By repeatedly selecting the smallest element and accumulating it in a new array, the Selection Sort algorithm effectively organizes the array into a sorted sequence.

## Example
Consider an array `[29, 10, 14, 37, 13]`. The selection sort algorithm will:

- First, find `10` as the smallest element and move it to the new array.
- Next, `13` is found as the next smallest element and moved.
- This process continues with `14`, `29`, and finally `37`.

The resulting sorted array will be `[10, 13, 14, 29, 37]`.
