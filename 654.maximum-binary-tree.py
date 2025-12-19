# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (86.22%)
# Likes:    5394
# Dislikes: 349
# Total Accepted:    350.9K
# Total Submissions: 407K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# You are given an integer array nums with no duplicates. A maximum binary tree
#
# can be built recursively from nums using the following algorithm:
# 
# 
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the
# maximum value.
# Recursively build the right subtree on the subarray suffix to the right of
# the maximum value.
# 
# Return the maximum binary tree built from nums.
# 
# Example 1:
# 
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right
# suffix is [0,5].
# ⁠   - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix
# is [2,1].
# ⁠       - Empty array, so no child.
# ⁠       - The largest value in [2,1] is 2. Left prefix is [] and right suffix
# is [1].
# ⁠           - Empty array, so no child.
# ⁠           - Only one element, so child is a node with value 1.
# ⁠   - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is
# [].
# ⁠       - Only one element, so child is a node with value 0.
# ⁠       - Empty array, so no child.
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
# 
# Constraints:
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.
# 
# @lc code=start
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        # num_copy=nums[:]
                  
        # nums = [3,2,1,6,0,5]

        # head=TreeNode(0)

        # def recursive(num_copy,head):

        #     # print("num_copy",num_copy)

        #     if not num_copy:

        #         return
            
        #     n=len(num_copy)

        #     max_element=-1000

        #     max_index=0

        #     for i in range(n):

        #         if max_element<num_copy[i]:

        #             max_element=num_copy[i]

        #             max_index=i

        #     # print("max_element",max_element)

        #     # print("max_index",max_index)


        #     head.val=max_element

        #     # print("head",head)

        #     if max_index!=0:

        #         head.left=TreeNode(0)

        #         recursive(num_copy[:max_index],head.left)

        #     if max_index!=n-1:

        #         head.right=TreeNode(0)

        #         recursive(num_copy[max_index+1:],head.right)


        # recursive(nums,head)

        # return head
    


test=Solution()
ans=test.constructMaximumBinaryTree([3,2,1,6,0,5])
print("ans",ans)
print(ans.val)


            
        
# @lc code=end

