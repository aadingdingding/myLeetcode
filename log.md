## Oct 27th - Arrays: Sliding Window
### Solved problems
* [59.spiral-matrix-ii](./arrays/spiral_matrix/59.spiral-matrix-ii.py)
* [76.spiral-matrix](./arrays/spiral_matrix/54.spiral-matrix.py)
### Summary
#### algrithom learning
We need to explicitly set up start/end column/row numbers as boundry. Be careful with the edge case when:  
1. start and end pointer value equals  
2. when the matrix is square, it's easier. When the matrix is reatangle, we need to be careful with boundry to make sure we don't revisit back.
#### python learning
* how to create a list: `arr = [0] * 5`.
* how to create a list of list:  
We cannot simply use `arr = [[0]] * 5` because all of list in arr is actually pointing to the same memory location (you can use `id()` to check memory location).  
1. simple for-loop:  
```
arr = []
for i in range(5):
    inner_arr = [0]
    arr.append(inner_arr)
```
2. list comprehension:  `arr = [[0] for _ in range(5)]`
3. numpy package:  
```
import numpy as np
lists = np.empty((10, 0)).tolist()
print(lists)
# [[], [], [], [], [], [], [], [], [], []]
```
## Oct 27th - Arrays: Sliding Window
### Solved problems
* [76.minimum-window-substring](./arrays/sliding_window/76.minimum-window-substring.py)
* [209.minimum-size-subarray-sum](/arrays/sliding_window/209.minimum-size-subarray-sum.py)
* [904.fruit-into-baskets](./arrays/sliding_window/904.fruit-into-baskets.py)
### Summary
#### algrithom learning
Sliding window is one type of two pointers which reduces the use of nested loops and replace it with a single loop, thereby reducing the time complexity. The key is to make sure we restrict the valid value within the sliding window. Usually we use fast pointer to find the valid substring/subarray and use left pointer to minimize the length.
#### python learning
* initialize set: `val = set()`.
* initialize hashmap: `dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}` or `dict = dict(key1='value1', key2='value2', key3='value3')`
* Counter in python: `collections.Counter()` - a Python library that counts the frequency of elements in a sequence. E.g. `collections.Counter('aadingding')` returns `Counter({'a': 2, 'i': 2, 'd': 2, 'g': 2, 'n': 2})`.

## Oct 25th - Arrays: Two Pointers
### Solved problems
* [26.remove-duplicates-from-sorted-array](./arrays/two_pointers/26.remove-duplicates-from-sorted-array.py)
* [27.remove-element](./arrays/two_pointers/27.remove-element.py)
* [283.move-zeroes](./arrays/two_pointers/283.move-zeroes.py)
* [844.backspace-string-compare](./arrays/two_pointers/844.backspace-string-compare.py)
* [977.squares-of-a-sorted-array](./arrays/two_pointers/977.squares-of-a-sorted-array.py)
### Summary
#### algrithom learning
Two pointers (also named as fast and slow pointers) is to replace a nested for-loop with one for-loop by using two pointers.
Slow pointer: pointe to the current index where we need to modify values.
Fast pointer: point to the elements we are looking for.
#### python learning
* always prefer to use `while(i<len(array))` for a loop instead of `for i in range(len(array))` because the second way always keep i incremental by 1. e.g. If in the loop when i=3, I use `i-=1`, the while loop recognize `i=2` while the for loop will keep use `i=3`.
* how to sort a list: `array.sort()` or `sorted(array)`.
* Be careful when using `&` - the `&` is a bitwise operator. Use `and` instead which is a logical boolean operator.