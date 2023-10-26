#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # # brute force
        # size = len(nums)
        # i=0
        # while i < size:
        #     if nums[i] == val:
        #         for j in range(i, size-1):
        #             nums[j] = nums[j+1]
                
        #         i -= 1
        #         size -= 1
        #     i += 1
        # return size

        #two pointers
        fast_index = 0
        slow_index = 0
        while fast_index < len(nums):
            if (nums[fast_index] != val):
                nums[slow_index] = nums[fast_index]
                slow_index += 1
            fast_index += 1

        return slow_index

        
# @lc code=end

