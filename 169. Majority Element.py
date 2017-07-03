from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = len(nums) >> 1
        count = defaultdict(int)
        for elem in nums:
            count[elem] += 1
            if count[elem] > major:
                return elem


# assert Solution().majorityElement([1, 2, 2, 1, 1, 2]) == 1 # but mine is null
assert Solution().majorityElement([1, 2, 2, 1, 1, 2, 2]) == 1
