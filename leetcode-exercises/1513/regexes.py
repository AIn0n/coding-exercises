import re

class Solution:
    MAX_CAP = 10**9 + 7

    def numSub(self, s: str) -> int:
        substrings = re.split("0+", s)
        res = 0
        for el in substrings:
            n = len(el)
            res += (n + 1) * n // 2
        return res % self.MAX_CAP
