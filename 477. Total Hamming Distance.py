class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * 32
        for elem in nums:
            i = 0
            while elem:
                if elem & 1:
                    count[i] += 1
                elem >>= 1
                i += 1
        n = len(nums)
        return sum((c * (n - c) for c in count))
