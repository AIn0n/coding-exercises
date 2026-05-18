def count_min_circular_dist(source: int, target: int, l: int) -> int:
    if source == target:
        return 0
    elif source > target:
        return min(source - target, l - source + target)
    else:
        return min(target - source, source + l - target)

class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        locations = tuple(idx for idx, el in enumerate(words) if el == target)
        if len(locations) == 0:
            return -1
        return min(count_min_circular_dist(startIndex, el, len(words)) for el in locations)

print(
    Solution().closestTarget(
        ["hello","i","am","leetcode","hello"],
        "hello",
        1
    )
)
