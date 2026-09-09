class Solution:
    def minWindow(self, s: str, t: str) -> str:  # Added 'self' here
        if not s or not t:
            return ""
        from collections import Counter
        t_c=Counter(t)
        missing=len(t)
        strt,end,left=0,0,0
        for right,char in enumerate(s):
            if t_c[char]>0:
                missing-=1
            t_c[char]-=1
            if missing==0:
                while left<right and t_c[s[left]]<0:
                    t_c[s[left]]+=1
                    left+=1
                if not end or (right-left)<(end-strt):
                    strt,end=left,right+1
                t_c[s[left]]+=1
                missing+=1
                left+=1
        return s[strt:end]
