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
            res.append(el)
        if carry:
            res.append(1)
        return list(reversed(res))
