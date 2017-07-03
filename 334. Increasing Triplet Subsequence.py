class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = min2 = float('inf')
        for elem in nums:
            if elem > min2:
                return True
            elif elem > min1:
                min2 = elem
            else:
                min1 = elem
        return False


assert Solution().increasingTriplet([1, 2, 3, 4, 5])
assert not Solution().increasingTriplet([5, 4, 3, 2, 1])
