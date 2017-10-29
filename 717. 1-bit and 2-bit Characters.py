class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = len(bits) - 2
        while i >= 0:
            if bits[i] == 0:
                return True
            elif bits[i - 1] == 0:
                return False
            i -= 2
        return True


print(Solution().isOneBitCharacter([1, 0, 0]))
print(Solution().isOneBitCharacter([1, 1, 1, 0]))
