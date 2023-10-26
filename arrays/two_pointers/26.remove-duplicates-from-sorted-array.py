#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow_pointer = 0
        fast_point = 1
        while fast_point < len(nums):
            if nums[fast_point] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_point]
            fast_point += 1

        return slow_pointer+1
            
        
# @lc code=end

