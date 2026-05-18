import re

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for el in set(s):
            palindromes = re.search(f"{el}(.+){el}", s)
            if palindromes is not None:
                res += len(set(palindromes.groups()[0]))
        return res

s = Solution()

print(s.countPalindromicSubsequence("ckafnafqo"))
print(s.countPalindromicSubsequence("aabca"))
print(s.countPalindromicSubsequence("bbcbaba"))