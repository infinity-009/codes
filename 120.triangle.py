#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (59.84%)
# Likes:    10679
# Dislikes: 605
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
# 
# 
# Example 1:
# 
# 
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

# Output: 11

# Explanation: The triangle looks like:

# ⁠   2

# ⁠  3 4
#  ⁠6 5 7
# 4 1 8 3

#  start

# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
# 
# Example 2:
# 
# Input: triangle = [[-10]]
# Output: -10
# 
# Constraints:
# 
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
# 
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#

## note the easiest solution is bottom up dp building solution incrementally.

from typing import List

# @lc code=start
import heapq

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n=len(triangle)
        print("n",n)
        # hp=[]

        # heapq.heappush(hp,(triangle[0][0],0,0))

        # ans=10**8

        # while hp:
        #     top=heapq.heappop(hp)

        #     print("top",top)

        #     cur_dist=top[0]

        #     # if cur_dist>=ans:
        #     #     continue

        #     if top[1]==n-1:
        #         ans=min(cur_dist,ans)

        #     if top[1]>=n-1:
        #         continue

        #     print(top[1]+1,   top[2])
        #     heapq.heappush(hp,(cur_dist+triangle[top[1]+1][top[2]],     top[1]+1,   top[2]))
        #     heapq.heappush(hp,(cur_dist+triangle[top[1]+1][top[2]+1],   top[1]+1,  top[2]+1))

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])

        return triangle[0][0]
    
# Input: 
triangle =[[-1],[2,3],[1,-1,-3]]

# Output: 11
test=Solution()

print("Output",test.minimumTotal(triangle))

## note the easiest solution is bottom up dp building solution incrementally.



                

# @lc code=end

