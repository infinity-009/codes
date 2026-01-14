#
# @lc app=leetcode id=3469 lang=python
#
# [3469] Find Minimum Cost to Remove Array Elements
#
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/description/
#
# algorithms
# Medium (21.09%)
# Likes:    143
# Dislikes: 9
# Total Accepted:    12.1K
# Total Submissions: 57.3K
# Testcase Example:  '[6,2,8,4]'
#
# You are given an integer array nums. Your task is to remove all elements from
# the array by performing one of the following operations at each step until
# nums is empty:
# 
# 
# Choose any two elements from the first three elements of nums and remove
# them. The cost of this operation is the maximum of the two elements
# removed.
# If fewer than three elements remain in nums, remove all the remaining
# elements in a single operation. The cost of this operation is the maximum of
# the remaining elements.
# 
# 
# Return the minimum cost required to remove all the elements.
# 
# 
# Example 1:
# 
# 
# Input: nums = [6,2,8,4]
# 
# Output: 12
# 
# Explanation:
# 
# Initially, nums = [6, 2, 8, 4].
# 
# 
# In the first operation, remove nums[0] = 6 and nums[2] = 8 with a cost of
# max(6, 8) = 8. Now, nums = [2, 4].
# In the second operation, remove the remaining elements with a cost of max(2,
# 4) = 4.
# 
# 
# The cost to remove all elements is 8 + 4 = 12. This is the minimum cost to
# remove all elements in nums. Hence, the output is 12.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,1,3,3,1]
# 
# Output: 5
# 
# Explanation:
# 
# Initially, nums = [2, 3, 2, 3,4,7] , 

# ans[n]=ans[n-1]+max(arr[n-2:]+[arr[n]])
# 
# 
# In the first operation, remove nums[0] = 2 and nums[1] = 1 with a cost of
# max(2, 1) = 2. Now, nums = [3, 3].
# In the second operation remove the remaining elements with a cost of max(3,
# 3) = 3.
# 
# 
# The cost to remove all elements is 2 + 3 = 5. This is the minimum cost to
# remove all elements in nums. Hence, the output is 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^6
# 
# @lc code=start
class Solution(object):
    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(2000)
        n = len(nums)
        memo = {}

        def dfs(i, j):
            if i >= n:
                return nums[j]
            if i == n - 1:
                return max(nums[j], nums[n - 1])
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 1. Remove j and i, keep i+1
            res1 = max(nums[j], nums[i]) + dfs(i + 2, i + 1)
            # 2. Remove j and i+1, keep i
            res2 = max(nums[j], nums[i+1]) + dfs(i + 2, i)
            # 3. Remove i and i+1, keep j
            res3 = max(nums[i], nums[i+1]) + dfs(i + 2, j)
            
            res = min(res1, res2, res3)
            memo[(i, j)] = res
            return res

        return dfs(1, 0)
        
         
        
        


test=Solution()

print("ans",test.minCost([2,1,3,3,1]))


# @lc code=end

