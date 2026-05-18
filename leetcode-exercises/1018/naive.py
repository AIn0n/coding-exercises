class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        res = []
        curr = 0
        for el in nums:
            curr = (curr << 1) + el
            res.append(curr % 5 == 0)
        return res