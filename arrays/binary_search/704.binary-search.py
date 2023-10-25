#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

# [1,4,5,7,9] 7

#  0,1,2,3,4
#  l   m   r
        
# @lc code=end

