#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # brute force
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        nums.sort()
        return nums
    
        # #two pointers
        # result = []
        # left, right = 0, len(nums) -1
        # while (left <= right):
        #     if abs(nums[left]) >= abs(nums[right]):
        #         result.append(nums[left]*nums[left])
        #         left += 1
        #     else:
        #         result.append(nums[right]*nums[right])
        #         right -= 1

        # return result[::-1]

# @lc code=end

