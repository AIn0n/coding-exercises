class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        new_s = s
        for _ in range(len(s)):
            new_s = new_s[1:] + new_s[:1]
            if new_s == goal:
                return True

        return False
