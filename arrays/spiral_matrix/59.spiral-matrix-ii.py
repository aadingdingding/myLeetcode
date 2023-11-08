#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0]*n for _ in range(n)]
        i = 1
        start_row, start_col, end_row, end_col = 0,0,n-1,n-1

        while start_row <= end_row and start_col <= end_col:
            # right
            for col in range(start_col, end_col+1):
                result[start_row][col] = i
                i += 1
            start_row += 1
            # down
            for row in range(start_row, end_row+1):
                result[row][end_col] = i
                i += 1
            end_col -= 1
            # left
            for col in range(end_col,start_col-1, -1):
                result[end_row][col] = i
                i += 1
            end_row -= 1
            # up
            for row in range(end_row, start_row-1, -1):
                result[row][start_col] = i
                i += 1
            start_col += 1

        return result
# @lc code=end