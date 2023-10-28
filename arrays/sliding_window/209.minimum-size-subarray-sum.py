#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left,right,sum = 0,0,0
        result = len(nums) + 1
        while (right < len(nums)):
            sum += nums[right]
            while (sum >= target):
                result = min(right - left + 1, result)
                sum -= nums[left]
                left += 1
            
            right += 1

        return result if result != (len(nums) + 1) else 0



# @lc code=end

