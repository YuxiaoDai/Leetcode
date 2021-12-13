#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# In Python, a string is immutable. You cannot overwrite the values of immutable objects.
# In order to overwrite string: 
# 1. convert string to list by list(str), 
# 2. do the operation and then 
# 3. convert list to string by ''.join(list)
# built in methods to reverse a string: str[::-1]

# @lc code=start
class Solution:

    def revrseSubStr(self, s: str) -> str:
        
        s = list(s)
        n = len(s)
        n_half = n//2
        for i in range(n_half):
            s[i],s[n - i - 1] = s[n - i - 1], s[i]
        
        return ''.join(s)

    def reverseStr(self, s: str, k: int) -> str:
        
        n = len(s)

        result = ''
        for i in range(0, n, k):
            if i + k > n:
                subStr = s[i : n]
            else:
                subStr = s[i : i+k]
            if i % (2*k) == 0:
                subStr = self.revrseSubStr(subStr)
            result += subStr
        
        return result



        
# @lc code=end

