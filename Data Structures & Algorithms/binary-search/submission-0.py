class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:  # Changed < to <= to handle single-element arrays
            mid = (left + right) // 2
            
            if nums[mid] == target:  # Check the array value, not the index
                return mid
            elif nums[mid] < target:  # Check the array value, not the index
                left = mid + 1
            else:
                right = mid - 1
                
        return -1  # Return integer -1 instead of string "-1"



