class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(map(lambda x: min(x % 3, 1), nums))