#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow_pointer = 0
        fast_pointer = 0
        while fast_pointer < len(nums):
            if nums[fast_pointer] != 0:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
            fast_pointer += 1

        for i in range(slow_pointer, len(nums)):
            nums[i] = 0

        return nums
        
# @lc code=end

