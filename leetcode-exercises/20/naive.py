class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for el in s:
            if el in "{[(":
                stack.append(el)
                continue
            if len(stack) == 0:
                return False
            head = stack.pop()
            if (
                (el == ")" and head != "(")
                or (el == "]" and head != "[")
                or (el == "}" and head != "{")
            ):
                return False
        return len(stack) == 0
