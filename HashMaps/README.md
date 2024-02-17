# Hash Tables

Hash tables, also known as hash maps, are data structures that implement an associative array abstract data type, a structure that can map keys to values. They work by using a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. Hash tables offer fast lookup, insertion, and deletion of key-value pairs, typically with an average time complexity of O(1) for these operations.
most of programming languages has implemented hash tables but with different names like in 
   <br> ` Python => dictionary ` <br>
    ` TypeScript => use the object as a hash table `<br>
    ` Rust => it called HashMap `<br>

## Implementation in Rust
```rust
// Creating a new hash table
let mut hash_table: HashMap<i32, &str> = HashMap::new();

// Inserting key-value pairs
hash_table.insert(1, "Value1");
hash_table.insert(2, "Value2");
hash_table.insert(3, "Value3");
```
## Implementation in Python
```python
# Using Python dictionaries to implement hash tables

# Creating a new hash table
hash_table = {}

# Inserting key-value pairs
hash_table[1] = "Value1"
hash_table[2] = "Value2"
hash_table[3] = "Value3"
```
## Implementation in TypeScript
```Typescript
// Using TypeScript objects to implement hash tables

// Creating a new hash table
const hashTable: { [key: number]: string } = {};

// Inserting key-value pairs
hashTable[1] = "Value1";
hashTable[2] = "Value2";
hashTable[3] = "Value3";

```
