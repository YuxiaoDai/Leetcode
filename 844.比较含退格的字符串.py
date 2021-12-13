#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        len_s = len(s)
        slow_s = 0
        for fast_s in range(len_s):
            if s[fast_s] != '#':
                s[slow_s] = s[fast_s]
                slow_s += 1
            else:
                slow_s -= 1
                slow_s = 0 if slow_s < 0 else slow_s
                
        result_s = ''.join(s[:slow_s])

        t = list(t)
        len_t = len(t)
        slow_t = 0
        for fast_t in range(len_t):
            if t[fast_t] != '#':
                t[slow_t] = t[fast_t]
                slow_t += 1
            else:
                slow_t -= 1
                slow_t = 0 if slow_t < 0 else slow_t
                
        result_t = ''.join(t[:slow_t])

        return result_s == result_t
a = Solution()
print(a.backspaceCompare('##a', 'ad#C'))


# @lc code=end

