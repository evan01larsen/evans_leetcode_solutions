# Constraints
# 2 <= nums.length < 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


class Solution(object):
    def twoSum(self, nums, target):

        # Create a dictionary to store the number and its index
        pair_idx = {}
        
        for i, num in enumerate(nums):
            # If the target value minus the current number exists as a value in pair_idx, 
            #   then return the indicies of the current number's index in enumerate(nums) and 
            #   the value of the key target-num
            if target - num in pair_idx:
                return [i, pair_idx[target-num]]
            # Otherwise, store the current number as a key and its index as the value in 
            # pair_idx for reference in the next loop
            pair_idx[num] = i

target = 9
nums = [2, 7, 11, 15]

target = 6
nums = [3, 2, 4]

ret = Solution().twoSum(nums, target)

print(ret)
