class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = False
        res = []
        digits[-1] += 1
        for el in reversed(digits):
            if carry:
                el += 1
                carry = False
            if el >= 10:
                el = el % 10
                carry = True
            res.insert(0, el)
        if carry:
            res.insert(0, 1)
        return res
