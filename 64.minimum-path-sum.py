# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,len(grid[0])):
            grid[0][i]+=grid[0][i-1]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])

        return grid[len(grid)-1][len(grid[0])-1]
# @lc code=end

