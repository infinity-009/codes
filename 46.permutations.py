#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (81.35%)
# Likes:    20558
# Dislikes: 373
# Total Accepted:    2.9M
# Total Submissions: 3.5M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        n=len(nums)

        def traverse(nums):

            if len(temp)==n:
                # print("temp",temp)
                ans.append(temp[:])
                return
            
            for i in range(len(nums)):
                temp.append(nums[i])
                # print("temp",temp)
                traverse(nums[:i]+nums[i+1:])
                temp.pop()
        traverse(nums[:])

        # print("ans",ans)
        return ans


# test=Solution()

# print(test.permute([1,2,3]))





        
# @lc code=end

