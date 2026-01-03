#
# @lc app=leetcode id=1247 lang=python3
#
# [1247] Minimum Swaps to Make Strings Equal
#
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
#
# algorithms
# Medium (65.09%)
# Likes:    1457
# Dislikes: 251
# Total Accepted:    49.8K
# Total Submissions: 76.5K
# Testcase Example:  '"xx"\n"yy"'
#
# You are given two strings s1 and s2 of equal length consisting of letters "x"
# and "y" only. Your task is to make these two strings equal to each other. You
# can swap any two characters that belong to different strings, which means:
# swap s1[i] and s2[j].
# 
# Return the minimum number of swaps required to make s1 and s2 equal, or
# return -1 if it is impossible to do so.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
# 
# 
# Example 2:
# 
# 
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we
# can only swap chars in different strings.
# 
# 
# Example 3:
# 
# 
# Input: s1 = "xx", s2 = "xy"
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 1000
# s1.length == s2.length
# s1, s2 only contain 'x' or 'y'.
# 
# 
#

# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:


        yx_count=0
        xy_count=0

        n=len(s1)
        m=len(s2)

        if n!=m:
            return -1

        for i in range(n):
            if s1[i]=='y' and s2[i]=='x':
                yx_count+=1
            elif s1[i]=='x' and s2[i]=='y':
                xy_count+=1 

        if yx_count%2!=xy_count%2:
            return -1
        
        return (yx_count//2) + (xy_count//2) + (2*(yx_count%2))

        
# @lc code=end

