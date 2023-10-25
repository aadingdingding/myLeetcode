#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x

        while (left <= right):
            mid = left + (right - left)//2
            if (mid * mid < x):
                left = mid + 1
            elif (mid * mid > x):
                right = mid -1
            else:
                return mid
            
        return left-1

# @lc code=end

