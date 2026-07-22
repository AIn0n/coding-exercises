revset_map = {"]": "[", ")": "(", "}": "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for el in s:
            if el in "{[(":
                stack.append(el)
                continue
            if len(stack) == 0 or revset_map.get(el, None) != stack.pop():
                return False
        return len(stack) == 0
