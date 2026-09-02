class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
   
        if not nums:
            return 0
            
        res = 0
        store = set(nums)  # O(1) lookups

        for num in nums:
            # ONLY start counting if 'num' is the absolute beginning of a sequence
            if (num - 1) not in store:
                streak = 0
                curr = num
                
                # Count consecutive numbers forward
                while curr in store:
                    streak += 1
                    curr += 1  # MUST BE INSIDE THE WHILE LOOP
                
                res = max(res, streak)
                
        return res
