# Constraints
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order

## Solution using older py

class Solution(object):
    def removeDuplicates(self, nums):

        if not nums: # Handle an empty list case
            return 0
        
        j = 0 # Pointer for the position of unique elements
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1 # Move to the next position
                nums[j] = nums[i]  # Assign the unique element

        # Return the length of the list with unique elements
        # The reason we add 1 is because it j intiially started at 0 
        return j + 1 
    
nums = [0, 0, 0, 1, 2, 3, 3, 4]   
ret = Solution().removeDuplicates(nums)
print(ret)

## First Version

class Solution(object):
    def removeDuplicates(self, nums):
        
        unique_nums = set()
        
        count = 0
        for num in nums:
            if num not in unique_nums:
                unique_nums.add(num)
                count += 1

        list_of_unique_nums = list(unique_nums)

        return count, list_of_unique_nums


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# count, list_of_nums = Solution().removeDuplicates(nums)

# print(f"{count},", list_of_nums)

## Second version

class Solution(object):
    def removeDuplicates(self, nums):
        
        unique_nums = []
        
        count = 0
        for num in nums:
            if num in unique_nums:
                pass
            else:
                unique_nums.append(num)
                count += 1

        return unique_nums


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# unique_nums = Solution().removeDuplicates(nums)

# print(unique_nums)