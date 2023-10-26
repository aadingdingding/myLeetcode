#
# @lc app=leetcode id=844 lang=python
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def getBackspaced(s):
            ans = ""
            fast_pointer = 0
            while fast_pointer < len(s):
                if s[fast_pointer] != '#':
                    ans += s[fast_pointer]
                else:
                    if len(ans) > 0:
                        ans = ans[:-1]
                fast_pointer += 1

            return ans

        backspaced_s = getBackspaced(s)
        backspaced_t = getBackspaced(t)
        print(backspaced_s)
        print(backspaced_t)
        return backspaced_s == backspaced_t
        
# @lc code=end

