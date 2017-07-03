class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_met = {}
        for i, elem in enumerate(nums):
            if elem in last_met and i - last_met[elem] <= k:
                return True
            last_met[elem] = i
        return False


Solution().containsNearbyDuplicate([2, 1, 2], 1)
Solution().containsNearbyDuplicate([2, 1, 2], 2)
