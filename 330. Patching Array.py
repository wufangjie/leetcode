class Solution(object):
    # [1, n - 1] n => 2n - 1
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)

        if length > 0 and nums[0] == 1:
            i, add = 1, 0
        else:
            i, add = 0, 1

        reach = 1
        while True:
            if reach >= n:
                return add
            if i < length and reach >= nums[i] - 1:
                reach += nums[i]
                i += 1
            else:
                reach = 2 * reach + 1
                add += 1



Solution().minPatches([1, 5, 10], 20)
Solution().minPatches([], 7)
