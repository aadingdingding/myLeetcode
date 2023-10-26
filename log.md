## Oct 25th - Arrays: Two pointer
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