"""
Elegant version with map, still slow as hell :/
"""


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        idxs = [idx for idx, el in  enumerate(nums) if el == 1]
        return all(map(lambda n: n[1] - n[0] > k, zip(idxs, idxs[1:])))