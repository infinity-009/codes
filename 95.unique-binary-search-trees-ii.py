#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (61.52%)
# Likes:    7909
# Dislikes: 580
# Total Accepted:    554.5K
# Total Submissions: 900.2K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List,Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

        def build_trees(st,end):

            if st>end: return [None]

            trees=[]

            for i in range(st,end+1):

                left_trees=build_trees(st,i-1)
                right_trees=build_trees(i+1,end)


                for l in left_trees:
                    for r in right_trees:
                        current_tree=TreeNode(i)
                        current_tree.left=l
                        current_tree.right=r
                        trees.append(current_tree)

            return trees
        
        return build_trees(1,n)




"""
Hello! I understand your confusion. Recursion with trees, especially when you have to generate *all possible structures* (not just traverse one), is tricky. It involves understanding how object references work and how to combine results from sub-problems.

Here is an in-depth explanation of how to approach this, what happens in memory, and the corrected solution.

### The Core Concept: Divide and Conquer

The key to solving "Unique BSTs" is not just simple traversal, but **Divide and Conquer**.

1.  **BST Property**: For any node with value `i`:
    *   All nodes in the **left** subtree must be smaller (`< i`).
    *   All nodes in the **right** subtree must be larger (`> i`).

2.  **The Strategy**:
    If we want to build all trees with numbers from `1` to `n`, we can iterate through every number `i` and treat it as the **root**.
    *   If `i` is the root, the **left** child must be built from numbers `[1, ... i-1]`.
    *   If `i` is the root, the **right** child must be built from numbers `[i+1, ... n]`.

### Visualizing the Recursion & References

Imagine `n = 3`. We have numbers `[1, 2, 3]`.

**Step 1: Pick a Root**
Let's say we pick **2** as the root.
*   Left side needs to handle `[1]`.
*   Right side needs to handle `[3]`.

**Step 2: Recursive Calls (The "Magic")**
Instead of passing a single `root` object down (which is where your current code gets stuck), the recursive function should **return a list of all possible subtrees**.

*   `generate(1, 1)` returns `[Node(1)]`.
*   `generate(3, 3)` returns `[Node(3)]`.

**Step 3: Cartesian Product (Combining References)**
Now we are back at Root **2**.
We have a list of possible lefts: `[Node(1)]`.
We have a list of possible rights: `[Node(3)]`.

We loop through every left option and every right option and attach them to a **new** node `2`.
```python
root = TreeNode(2)
root.left = left_option  # Reference to Node(1)
root.right = right_option # Reference to Node(3)
```

### Why your current approach was difficult
In your code, you were trying to pass a single `root` object down (`backtrack(..., root)`).
*   **The Problem**: You need to return *multiple* different trees. If you modify `root.left` in one recursive call, it modifies it for *everyone* holding a reference to that `root`.
*   **The Fix**: Don't pass the node down. Instead, build the nodes **bottom-up** and return lists of trees.

### The Correct Implementation

Here is the corrected code. I have replaced the inner logic to use the helper function `build_trees(start, end)`.

```python
# ...existing code...
from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        # Helper function that returns a LIST of trees (roots)
        # that can be formed using numbers from start to end.
        def build_trees(start, end):
            # Base Case: If start > end, there are no numbers left.
            # We return [None] because a leaf node's child is None.
            # This is crucial for the loops below to run at least once.
            if start > end:
                return [None]
            
            all_trees = []
            
            # Pick every number 'i' in the range as the root
            for i in range(start, end + 1):
                
                # 1. Generate all possible left subtrees from numbers smaller than i
                left_subtrees = build_trees(start, i - 1)
                
                # 2. Generate all possible right subtrees from numbers larger than i
                right_subtrees = build_trees(i + 1, end)
                
                # 3. Connect the current root 'i' with every combination 
                #    of left and right subtrees.
                for l in left_subtrees:
                    for r in right_subtrees:
                        current_tree = TreeNode(i)
                        current_tree.left = l   # Link reference
                        current_tree.right = r  # Link reference
                        all_trees.append(current_tree)
            
            return all_trees

        return build_trees(1, n)
# @lc code=end
```

### How to approach these problems (Mental Model)

When you see "Return all possible..." or "Generate all structures..." involving trees:

1.  **Think Recursive Definition**: A tree is just `Root + Left Subtree + Right Subtree`.
2.  **Define the Function Signature**: Instead of `void traverse(root)`, think `List<Node> generate(range)`.
3.  **Identify the Split Point**: In BSTs, the split point is the root value `i`. Everything left of `i` goes to the left recursion; everything right goes to the right.
4.  **Handle Base Cases**: What happens if the range is empty? (Return `[None]`). What happens if it's a single number? (Return `[Node(val)]`).
5.  **Combine**: Use nested loops to combine results. This is similar to finding all pairs `(x, y)` where `x` comes from the left results and `y` comes from the right results.

### About Object References
In the code above:
*   `l` is a reference to a tree node created deeper in the recursion.
*   When we do `current_tree.left = l`, we are pointing the new node's left arm to that existing object.
*   **Sharing**: If `left_subtrees` has only one option (e.g., node `1`), but `right_subtrees` has 5 options, we will create 5 new roots, but they will **all share the exact same object** for their left child. This is efficient and safe because we don't modify the children after creation.
"""
# @lc code=end

