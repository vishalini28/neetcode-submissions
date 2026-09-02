class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
            
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        total_water = 0
        
        while left < right:
            # Move the pointer with the smaller boundary wall
            if heights[left] < heights[right]:
                left += 1
                # Update the tallest wall seen on the left
                left_max = max(left_max, heights[left])
                # Water trapped on this specific bar
                total_water += left_max - heights[left]
            else:
                right -= 1
                # Update the tallest wall seen on the right
                right_max = max(right_max, heights[right])
                # Water trapped on this specific bar
                total_water += right_max - heights[right]
                
        return total_water
