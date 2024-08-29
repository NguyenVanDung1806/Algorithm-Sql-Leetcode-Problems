# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []#tao mot dictionary de chua 3 so co total = 0 sau do sap xep theo chieu tang dan equa .sort
        nums.sort()
        length = len(nums) #tao mot bien length = do dai nums
        for i in range(length - 2): # duyet i cho den length - 2 de giu lai gia tri cho left va right
            if i > 0 and nums[i] == nums[i - 1]: # i > 0 va vi tri thu i ma trung voi vi tri thu i + 1 tuc la no da duoc xem xet qua
                continue
            left = i + 1 
            right = length - 1
            while left < right: 
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]]) # add nhung gia tri thoa dieu kien vao biesn res
                    while left < right and nums[left] == nums[left + 1]: # quan trong la minh da check qua no chua va tiep tuc tang gia tri de so khop
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

                
        