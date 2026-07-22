from itertools import takewhile


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        return "".join(el[0] for el in takewhile(lambda x: len(set(x)) == 1, zip(*strs)))
