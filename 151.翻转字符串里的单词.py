#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:

    #删去多余空格
    def trimSpaces(self, s):

        #删去头部空格
        n = len(s)
        left = 0
        right = n-1
        while left<=right and s[left]==' ':       
            left+=1
        s = s[left:]

        #删去尾部空格
        n = len(s)
        left = 0
        right = n-1
        while left<=right and s[right]==' ':        #去除结尾的空格
            right=right-1
        s = s[:right+1]

        #删去中间空格
        n = len(s)
        slow = 0
        for fast in range(n):
            if s[fast] != " " or (s[fast] == " " and s[fast + 1] != " "):
                s[slow] = s[fast]
                slow += 1

        return(s[:slow])

    def reverseString(self, s):
        n = len(s)
        n_half = n//2 

        for i in range(n_half):
            right = i
            left = n - 1 - i
            s[right], s[left] = s[left], s[right]

        return s

    def reverseWords(self, s: str) -> str:
        s_list = list(s)
        trimedString = self.trimSpaces(s_list)
        reversedString = self.reverseString(trimedString)

        n = len(reversedString)
        start = 0
        for end in range(n):
            if reversedString[end] == ' ': 
                reversedString[start:end] = self.reverseString(reversedString[start:end])
                start = end + 1
            elif end == n-1:
                reversedString[start:end+1] = self.reverseString(reversedString[start:end+1])
                
        
        return ''.join(reversedString)


a = Solution()
s = list("  hello  world ")
print(a.trimSpaces(s))
print(a.reverseWords(s))
        
        

# @lc code=end

