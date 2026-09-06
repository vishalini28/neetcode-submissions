class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_l=0
        max_f=0
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            max_f=max(max_f,count[s[right]])
            if (right-left+1)-max_f>k:
                count[s[left]]-=1
                left+=1
            max_l=max(max_l,right-left+1)
        return max_l

        