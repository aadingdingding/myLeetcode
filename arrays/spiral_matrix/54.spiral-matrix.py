#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        result = []
        start_row, start_col, end_row, end_col = 0,0,m-1,n-1

        while start_col <= end_col or start_row <= end_row:
            # right
            if start_row <= end_row:
                for col in range(start_col, end_col+1):
                    result.append(matrix[start_row][col])
            start_row += 1
            # down
            if start_col <= end_col:
                for row in range(start_row, end_row+1):
                    result.append(matrix[row][end_col])
            end_col -= 1
            # left
            if start_row <= end_row:
                for col in range(end_col, start_col-1, -1):
                    result.append(matrix[end_row][col])
            end_row -= 1
            # up
            if start_col <= end_col:
                for row in range(end_row, start_row-1, -1):
                    result.append(matrix[row][start_col])
            start_col += 1
        
        return result
# @lc code=end
