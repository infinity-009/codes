#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        total = m * n
        st = 0
        end = total - 1

        while st <= end:
            mid = (st + end) // 2
            x = mid // n
            y = mid % n
            
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid - 1
            else:
                st = mid + 1
                
        return False
        
# @lc code=end