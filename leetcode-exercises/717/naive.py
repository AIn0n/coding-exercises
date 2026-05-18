class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        pointer = 0
        while pointer < len(bits) - 1:
            if bits[pointer] == 0:
                pointer += 1
            if bits[pointer] == 1:
                pointer += 2
        
        return pointer != len(bits)