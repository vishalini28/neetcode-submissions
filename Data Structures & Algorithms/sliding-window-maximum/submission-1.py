from collections import deque
class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if not nums or k==0:
        return []
    res=[]
    window=deque()
    for i,num in enumerate(nums):
        if window and window[0]<i-k+1:
            window.popleft()
        while window and nums[window[-1]]<num:
            window.pop()
        window.append(i)
        if i>=k-1:
            res.append(nums[window[0]])
    return res


    

