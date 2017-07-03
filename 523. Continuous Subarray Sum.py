class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        if k == 0:
            i = 0
            while i < n - 1:
                if nums[i] == 0:
                    if nums[i + 1] == 0:
                        return True
                    i += 1
                i += 1
            return False

        mods = set()
        cur = 0
        for i in range(1, n):
            mods.add((nums[i - 1] - cur) % k)
            if (-cur - nums[i]) % k in mods:
                return True
            cur += nums[i]
        return False

        # each element construct set is costly, use a cur instead, above
        # beats 11.97% vs 87.58%
        # mods = set()
        # for i in range(1, n):
        #     mods.add(nums[i - 1] % k)
        #     mods = {(m + nums[i]) % k for m in mods}
        #     if 0 in mods:
        #         return True
        # return False


assert Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
assert Solution().checkSubarraySum([23, 2, 6, 4, 7], 6)
assert not Solution().checkSubarraySum([23, 2, 6, 4, 7], 0)
assert Solution().checkSubarraySum([23, 2, 6, 4, 7, 0, 0], 0)
