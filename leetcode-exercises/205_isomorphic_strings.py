from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in mapping.values():
                mapping[t[i]] = s[i]
        return "".join(mapping[c] for c in t) == s
    
sol = Solution()

print(sol.isIsomorphic("badc", "baba"))