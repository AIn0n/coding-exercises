class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return sum(map(lambda x: 1 if x % 3 else 0, nums))