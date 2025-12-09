#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (81.72%)
# Likes:    18836
# Dislikes: 333
# Total Accepted:    2.8M
# Total Submissions: 3.4M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# Example 2:
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# Constraints:
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# @lc code=start

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

    # Input: nums = [1,2,3]

    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        ans=[]
        n=len(nums)
        st=[]
        def backtracking(i):
            
            ans.append(st[:])

            for j in range(i,n):

                st.append(nums[j]) 

                backtracking(j+1)

                st.pop()

        backtracking(0)

        return ans
        

test=Solution()

print(test.subsets([1,2,3,4,5,6,7,8]))
# @lc code=end

