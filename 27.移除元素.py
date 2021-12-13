#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
# 用慢指针来记录有符合条件的数，用快指针来循环
# @lc code=start
class Solution:
    def removeElement(self, nums, val: int) -> int:

        n = len(nums)

        slow = 0
        fast = 0

        while fast <= n-1:
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1

        return slow

#a = Solution()
#print(a.removeElement([2],3))               

# @lc code=end

