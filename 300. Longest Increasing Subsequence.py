class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            temp = [dp[j] for j in range(i) if nums[j] < nums[i]]
            if temp:
                dp[i] = 1 + max(temp) # python2 max do not support default
        return max(dp)


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])

# cannot come up with nlog(n) solution


import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        rlt = []
        for i in nums:
            n = bisect.bisect_left(rlt, i)
            if n == len(rlt):
                rlt.append(i)
            else:
                rlt[n] = i
        return len(rlt)
