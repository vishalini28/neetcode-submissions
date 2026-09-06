class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        len1=len(s1)
        for i in range(len(s2)-len1+1):
            substr=s2[i:i+len1]
            substr=sorted(substr)
            if s1==substr:
                return True
        return False