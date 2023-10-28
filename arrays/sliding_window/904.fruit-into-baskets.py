#
# @lc app=leetcode id=904 lang=python
#
# [904] Fruit Into Baskets
#

# @lc code=start
import collections

# translate the long problem description into:
# We need to find the longest subarray from the fruits
# array where the longest subarray should only contain
# two distinct integers. Return the length of the longest
# array.

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        result = 0
        start,end=0,0
        basket = collections.defaultdict(int)

        while end < len(fruits):
            basket[fruits[end]] += 1

            while len(basket) > 2:
                fruitType = fruits[start]
                basket[fruitType] -= 1
                if basket[fruitType] == 0:
                    basket.pop(fruitType)
                start += 1
                
            result = max(result, end - start + 1)
            end += 1

        return result
# @lc code=end

