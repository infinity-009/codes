#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (63.02%)
# Likes:    10919
# Dislikes: 443
# Total Accepted:    825.4K
# Total Submissions: 1.3M
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
# 


# Example 1:
# 
# Input: n = 3
# Output: 5
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# Constraints:
# 1 <= n <= 19
# 
"""
n=2

1,2,null
1,null,2
2,1,null
2,null,1

"""

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:

        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):

            for j in range(0,i):
                dp[i]+=dp[j]*dp[i-j-1]

        print("dp",dp)
        return dp[n]


test=Solution()

print("answer",test.numTrees(3))
        
# @lc code=end



"""

Here is the explanation for ** Unique Binary Search Trees ** from fundamental principles.

### 1. Deconstructing the Problem

The core of this problem lies in the definition of a Binary Search Tree (BST).
**Fundamental Principle:** For any node chosen as the **Root**:
1.  All nodes in the **Left Subtree** must be smaller than the Root.
2.  All nodes in the **Right Subtree** must be larger than the Root.

This definition forces a strict structure. If you have numbers `1` to `n` and you pick number `i` as the root:
*   The **Left** side *must* consist of the numbers `1` to `i-1`.
*   The **Right** side *must* consist of the numbers `i+1` to `n`.

### 2. Mental Sandbox: Trying Solutions

Let's build this up from the simplest cases to see the pattern.

**Case n = 0:**
*   An empty tree is still a valid BST structure.
*   **Count:** 1

**Case n = 1:**
*   Only one option: Node `1` is root.
*   **Count:** 1

**Case n = 2:** (Nodes: 1, 2)
*   *Option A (Root is 1):* Left is empty (0 nodes). Right has {2} (1 node).
    *   Combinations: `Count(0) * Count(1)` = $1 * 1 = 1$.
*   *Option B (Root is 2):* Left has {1} (1 node). Right is empty (0 nodes).
    *   Combinations: `Count(1) * Count(0)` = $1 * 1 = 1$.
*   **Total:** $1 + 1 = 2$.

**Case n = 3:** (Nodes: 1, 2, 3)
*   *Root is 1:* Left has {} (0 nodes). Right has {2, 3} (2 nodes).
    *   Combinations: `Count(0) * Count(2)` = $1 * 2 = 2$.
*   *Root is 2:* Left has {1} (1 node). Right has {3} (1 node).
    *   Combinations: `Count(1) * Count(1)` = $1 * 1 = 1$.
*   *Root is 3:* Left has {1, 2} (2 nodes). Right has {} (0 nodes).
    *   Combinations: `Count(2) * Count(0)` = $2 * 1 = 2$.
*   **Total:** $2 + 1 + 2 = 5$.

### 3. The "Aha!" Moment (Abstraction)

You might be tempted to think about the specific numbers (like "how do I arrange 2 and 3?").
**Stop thinking about values.** Think about **quantities**.

The number of ways to arrange the set `{2, 3}` into a BST is exactly the same as arranging `{1, 2}` or `{99, 100}`.
If you have `k` nodes, the number of unique BSTs depends *only* on `k`, not on the values themselves.

This means if we know the answer for `n=0`, `n=1`, and `n=2`, we can calculate `n=3` using simple math, without actually building the trees.

### 4. The Thought Process (Dynamic Programming)

Your current code attempts to use `backtrack` with a `set`. This suggests you are trying to generate permutations. However, this is inefficient because we don't need to *see* the trees, we just need to *count* them.

**The Cartesian Product Principle:**
If there are $L$ ways to form the left subtree and $R$ ways to form the right subtree, the total ways to form the whole tree with that specific root is $L \times R$.

**The Algorithm:**
To find `G(n)` (the number of unique BSTs for `n` nodes):
1.  Create an array `dp` of size `n + 1` to store the counts.
2.  Initialize `dp[0] = 1` and `dp[1] = 1`.
3.  Loop from `i = 2` up to `n` (to fill our table).
4.  Inside that, loop through every number `j` from `1` to `i` (treating `j` as the root).
    *   Nodes on left: `j - 1`
    *   Nodes on right: `i - j`
    *   `dp[i] += dp[left] * dp[right]`

This approach is mathematically known as the **Catalan Numbers**.

### Summary
1.  **Don't build the trees.** It's too slow.
2.  **Break it down by Root.** Picking a root splits the problem into two independent sub-problems (Left size vs Right size).
3.  **Multiply possibilities.** Total = (Ways Left) * (Ways Right).
4.  **Sum over all roots.** Iterate through every possible root (1 to n) and sum up the totals.



"""

