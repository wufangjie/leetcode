import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        sorted_right = []
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(sorted_right, nums[i])
            result[i] = idx
            sorted_right.insert(idx, nums[i])
        return result


Solution().countSmaller([5,2,1,1,1,6,1,1,1])
