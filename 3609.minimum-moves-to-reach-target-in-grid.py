#
# @lc app=leetcode id=3609 lang=python
#
# [3609] Minimum Moves to Reach Target in Grid
#
# https://leetcode.com/problems/minimum-moves-to-reach-target-in-grid/description/
#
# algorithms
# Hard (14.60%)
# Likes:    54
# Dislikes: 3
# Total Accepted:    4.9K
# Total Submissions: 33.8K
# Testcase Example:  '1\n2\n5\n4'
#
# You are given four integers sx, sy, tx, and ty, representing two points (sx,
# sy) and (tx, ty) on an infinitely large 2D grid.
# 
# You start at (sx, sy).
# 
# At any point (x, y), define m = max(x, y). You can either:
# 
# 
# Move to (x + m, y), or
# Move to (x, y + m).
# 
# 
# Return the minimum number of moves required to reach (tx, ty). If it is
# impossible to reach the target, return -1.
# 
# 
# Example 1:
# 
# 
# Input: sx = 1, sy = 2, tx = 5, ty = 4
# 
# Output: 2
# 
# Explanation:
# 
# The optimal path is:
# 
# 
# Move 1: max(1, 2) = 2. Increase the y-coordinate by 2, moving from (1, 2) to
# (1, 2 + 2) = (1, 4).
# Move 2: max(1, 4) = 4. Increase the x-coordinate by 4, moving from (1, 4) to
# (1 + 4, 4) = (5, 4).
# 
# 
# Thus, the minimum number of moves to reach (5, 4) is 2.
# 
# 
# Example 2:
# 
# 
# Input: sx = 0, sy = 1, tx = 2, ty = 3
# 
# Output: 3
# 
# Explanation:
# 
# The optimal path is:
# 
# 
# Move 1: max(0, 1) = 1. Increase the x-coordinate by 1, moving from (0, 1) to
# (0 + 1, 1) = (1, 1).
# Move 2: max(1, 1) = 1. Increase the x-coordinate by 1, moving from (1, 1) to
# (1 + 1, 1) = (2, 1).
# Move 3: max(2, 1) = 2. Increase the y-coordinate by 2, moving from (2, 1) to
# (2, 1 + 2) = (2, 3).
# 
# 
# Thus, the minimum number of moves to reach (2, 3) is 3.
# 
# 
# Example 3:
# 
# 
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# 
# Output: -1
# 
# Explanation:
# 
# 
# It is impossible to reach (2, 2) from (1, 1) using the allowed moves. Thus,
# the answer is -1.
# 
# Constraints:
# 
# 
# 0 <= sx <= tx <= 10^9
# 0 <= sy <= ty <= 10^9
# 
# 
#

# @lc code=start
class Solution(object):
    def minMoves(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: int
        
                             x,y
                             
        
              2x,y                    x,y+x
        
        
        4x,y | 2x,y+2x            2x+y,y+x | x,2y+2x
        
        
        
        """
        
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(sx,sy,tx,ty):
            
            # print(sx,sy,tx,ty)
            
            maxx=max(sx,sy)
            
            if sx>tx or sy>ty :
                return None
            
            if sx==tx and sy==ty:
                return 0
            
            result_1=dfs(sx+maxx,sy,tx,ty)
            result_2=dfs(sx,sy+maxx,tx,ty)
            
            # print("resss",result_1,result_2)
            
            if result_1 is not None and result_2 is not None:
                return 1 + min(result_1, result_2)
            elif result_1 is not None: 
                return 1 + result_1
            elif result_2 is not None:
                return 1 + result_2
            else:
                return None
                        
        ans=dfs(sx,sy,tx,ty)
        if ans :
            return ans 
        return -1
            
            
test=Solution()

print("ans",test.minMoves(1,1,2,2))
            
            
        
        
        
        
        
        
# @lc code=end

