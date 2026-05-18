class Solution:

    MAX_CAP = 10**9 + 7

    def partition(t, s: str, stopper: str = "0"):
        res = ""
        for el in s:
            if el == stopper:
                if len(res) > 0:
                    yield res
                    res = ""
                continue
            res += el
        yield res


    def numSub(self, s: str) -> int:
        substrings = self.partition(s)
        res = 0
        for el in substrings:
            n = len(el)
            if n == 1:
                res += 1
            else:
                res += (n + 1) * n // 2
        return res % self.MAX_CAP
        