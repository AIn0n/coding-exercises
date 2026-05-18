class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        idxs = [idx for idx, el in  enumerate(nums) if el == 1]
        for idx1, idx2 in zip(idxs, idxs[1:]):
            if idx2 - idx1 <= k:
                return False
        return True
