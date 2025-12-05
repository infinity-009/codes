#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        left_depth = 0
        right_depth = 0
        left_node = root
        right_node = root

        is_complete=False
        
        while left_node or right_node:
            
            depth += 1
            left_node = left_node.left
            right_node = right_node.right
        
        if left_depth==right_depth:
            return 2**left_depth -1
        
        return 1+self.countNodes(root.left)+self.countNodes(root.right)




           
        
# @lc code=end

