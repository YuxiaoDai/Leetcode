#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# Python Add Elements to Array:
# Python doesn’t have a specific data type to represent arrays.
# The following can be used to represent arrays in Python:
# 1. By using lists
# 1.1 append: [1,2,3].append(4) -> [1,2,3,4]; [1,2,3].append([4,5]) -> [1,2,3,[4,5]]
# 1.2 extend: [1,2,3].extend([4,5]) -> [1,2,3,4,5]
# 1.3 insert: [1,2,3].insert(0,10) -> [10,1,2,3]
# 2. By using the numpy array
# 2.1 append: np.append([1,2,3], [4,5]) -> [1,2,3,4,5]
# 2.2 insert: np.insert([1,2,3], 0, 10) -> [10,1,2,3]
# @lc code=start
class Solution:
    def sortedSquares(self, nums):
        result = []

        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            l_sqr = nums[l]*nums[l]
            r_sqr = nums[r]*nums[r]
            if l_sqr > r_sqr:
                result.append(l_sqr)
                l += 1
            elif l_sqr < r_sqr:
                result.append(r_sqr)
                r -= 1
            else:
                if(l == r):
                    result.append(l_sqr)
                else:
                    result.extend([l_sqr, r_sqr])
                l += 1
                r -= 1
        return result[::-1]
        
a = Solution()
    
print(a.sortedSquares([-4,-1,0,3,10]))
        
# @lc code=end

