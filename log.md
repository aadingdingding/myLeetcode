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