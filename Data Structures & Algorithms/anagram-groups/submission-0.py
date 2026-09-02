from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v=defaultdict(list)
        for s in strs:
            sorted_words="".join(sorted(s))
            v[sorted_words].append(s)
        return list(v.values())

        