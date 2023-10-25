#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1:
        # left, right = 0, len(nums)-1
        # while (left<=right):
        #     mid = left + (right-left)//2
        #     if (nums[mid]>target):
        #         right =  mid-1
        #     elif (nums[mid]<target):
        #         left = mid+1
        #     else:
        #         left = mid
        #         right = mid
        #         while (left>=0 and nums[left] == target):
        #             left -= 1
        #         while (right < len(nums) and nums[right] == target):
        #             right += 1
                
        #         return [left+1, right-1]
            
        # return [-1, -1]

        # Solution 2:
        def findLeft(nums, target):
            left, right = 0, len(nums)-1

            while (left<=right):
                mid = left + (right - left)//2
                if (nums[mid] > target):
                    right = mid - 1
                elif (nums[mid] < target):
                    left = mid + 1
                else:
                    if mid == 0 or (nums[mid-1] != nums[mid]):
                        return mid
                    else: right = mid-1
            return -1

        def findRight(nums, target):
            left, right = 0, len(nums)-1

            while (left<=right):
                mid = left + (right - left)//2
                if (nums[mid] > target):
                    right = mid - 1
                elif (nums[mid] < target):
                    left = mid + 1
                else:
                    if mid == len(nums)-1 or (nums[mid+1] != nums[mid]):
                        return mid
                    else: left = mid+1

            return -1


        return [findLeft(nums, target), findRight(nums, target)]
    
# @lc code=end

