#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.56%)
# Likes:    9019
# Dislikes: 160
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start

from typing import List

class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans=set()
        temp=[]
        n=len(nums)

        def traverse(nums):

            if len(temp)==n:
                # print("temp",temp)
                ans.append(tuple(temp[:]))
                return
            
            for i in range(len(nums)):
                temp.append(nums[i])
                # print("temp",temp)
                traverse(nums[:i]+nums[i+1:])
                temp.pop()
        traverse(nums[:])

        # print("ans",ans)
        x=[]
        for s in ans:
            x.append(list(s))
        return x
# @lc code=end

