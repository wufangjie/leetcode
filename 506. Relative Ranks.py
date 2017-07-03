class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        idx = sorted(range(n), key=lambda x: nums[x], reverse=True)
        idx2 = sorted(range(n), key=lambda x: idx[x])
        result = (["Gold Medal", "Silver Medal", "Bronze Medal"]
                  + [str(i) for i in range(4, n + 1)])
        return [result[i] for i in idx2]
