class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(31, -1, -1):
            answer <<= 1
            prefixes = {num >> i for num in nums}
            better = answer ^ 1
            answer ^= any(better ^ p in prefixes for p in prefixes)
        return answer
