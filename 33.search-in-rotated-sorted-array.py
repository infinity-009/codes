#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        st=0
        ed=len(nums)-1

        while st<=ed:
            mid=(st+ed)//2
            if nums[mid]==target:
                return mid
            
            elif(nums[st]<=nums[mid]):  ## if mid is in left sorted half
                if nums[st]<=target<=nums[mid]:
                    ed=mid-1
                else:
                    st=mid+1
            else:                      ## if mid is in right sorted half
                if nums[mid]<=target<=nums[ed]:
                    st=mid+1
                else:
                    ed=mid-1
        
        return -1
# @lc code=end

