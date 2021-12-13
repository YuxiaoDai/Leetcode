#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        
        n = len(nums)
        slow = 0
        
        for fast in range(n):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
                
# @lc code=end

#a = Solution()
#print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))