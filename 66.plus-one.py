#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                if i<=1 and digits[0]==9:
                    digits[i]=digits[0]=0
                    return [1]+digits
                if i==1:
                    digits[i]=0
                    digits[0]+=1
                    return digits
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return digits
# @lc code=end

