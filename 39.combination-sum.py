#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))  # Append a copy of the valid combination
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # Choose the current candidate
                path.append(candidates[i])   #update array in place
                # Explore further with the reduced target
                backtrack(i, target - candidates[i], path)
                # Backtrack: undo the choice
                path.pop() #pop  that element after checking all the combinations.

        result = []
        candidates.sort()  # Optional for pruning in other cases
        backtrack(0, target, [])
        return result
        
# @lc code=end
