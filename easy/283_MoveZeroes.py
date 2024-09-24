# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def MoveZeros(self , nums):
    prev_idx = 0 #tao gia tri dau bang 0 
    for i in range(len(nums)):
        if nums[i] !=0:
            hold = nums[prev_idx]
            nums[prev_idx] = nums[i]
            nums[i] = hold
            nums[prev_idx] += 1
            
# Bắt đầu với prev_idx = 0.
# i = 0: nums[0] là 0, không làm gì cả.
# i = 1: nums[1] là 1, không phải 0, hoán đổi nums[0] với nums[1]. Danh sách trở thành [1, 0, 0, 3, 12], và prev_idx tăng lên 1.
# i = 2: nums[2] là 0, không làm gì cả.
# i = 3: nums[3] là 3, không phải 0, hoán đổi nums[1] với nums[3]. Danh sách trở thành [1, 3, 0, 0, 12], và prev_idx tăng lên 2.
# i = 4: nums[4] là 12, không phải 0, hoán đổi nums[2] với nums[4]. Danh sách trở thành [1, 3, 12, 0, 0], và prev_idx tăng lên 3.
