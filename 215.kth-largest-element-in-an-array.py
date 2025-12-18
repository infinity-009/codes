from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
        # while True:
        #     n=len(nums)
        #     pivot=nums[0]

        #     # print("pivot",pivot)
        #     left_arr=[]
        #     right_arr=[]
        #     # print("nums",nums)
        #     equal_count=0
        #     for i in range(n):
        #         if nums[i]<pivot:
        #             left_arr.append(nums[i])
        #         elif nums[i]>pivot:
        #             right_arr.append(nums[i])
        #         else:
        #             equal_count+=1


        #     # print("left_arrr",left_arr)
        #     # print("right_arrr",right_arr)
        #     left_count=len(left_arr)
        #     right_count=len(right_arr)
            
        #     # This condition checks if k is within the pivots range
        #     if k > right_count and k <= right_count + equal_count:
        #         return pivot

        #     # print("k",k)
        #     if right_count>=k:
        #         nums=right_arr
        #     else:
        #         nums=left_arr
        #         # We must subtract both larger elements and equal elements to find the index in 
        #         k = k - right_count - equal_count