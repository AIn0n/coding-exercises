from itertools import chain
from typing import Iterable


def count_circular_dists(source: int, target: int, l: int) -> Iterable[int]:
    if source == target:
        return [0]
    elif source > target:
        return source - target, l - source + target
    else:
        return target - source, source + l - target


class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        locations = tuple(idx for idx, el in enumerate(words) if el == target)
        if len(locations) == 0:
            return -1
        return min(
            chain.from_iterable(
                map(
                    lambda x: count_circular_dists(x, startIndex, len(words)), locations
                )
            )
        )


print(Solution().closestTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
