import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = right
        
        while left <= right:
            mid = (left + right) // 2
            tot_hrs = 0
            
            for pile in piles:
                # Use math.ceil for precise rounding up with large numbers
                tot_hrs += math.ceil(pile / mid)
                
            if tot_hrs <= h:
                speed = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return speed
