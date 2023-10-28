#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections
import sys


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        count = collections.Counter(t)
        start, end = 0, 0
        minLength = sys.maxint
        result = ""
        totalChar = len(count)

        while end < len(s):
            while end < len(s) and totalChar != 0:
                if s[end] in count:
                    count[s[end]] -= 1
                    if count[s[end]] == 0:
                        totalChar -= 1
                
                end += 1

            while start < end and totalChar == 0:
                if end - start < minLength:
                    minLength = end - start
                    result = s[start:end]

                if s[start] in count:
                    count[s[start]] += 1
                    if count[s[start]] > 0:
                        totalChar += 1
                
                start += 1

        return result
# @lc code=end

