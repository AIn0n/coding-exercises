from itertools import accumulate as acc

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        res = map(lambda x : x % 5 == 0, acc(nums, lambda a, el: (a << 1) + el, initial=0))
        return list(res)[1:]
