class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre, pre_idx = 1, 0
        count = 0
        for i, elem in enumerate(nums):
            for pre_idx in range(pre_idx, i + 1):
                if elem * pre < k:
                    break
                pre //= nums[pre_idx]
            else:
                pre, pre_idx = 1, i + 1
                continue

            pre *= elem
            count += i - pre_idx + 1
        return count


print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
