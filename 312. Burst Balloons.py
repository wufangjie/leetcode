from utils import memo


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [elem for elem in nums if elem > 0]
        if not nums:
            return 0
        n = len(nums)
        nums.append(1)
        dp = []

        for i in range(n):
            dp.append([0] * (i + 1))
            dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]
            for j in range(i - 1, -1, -1):
                left_right = nums[j - 1] * nums[i + 1]
                theMax = max(dp[i][j + 1] + left_right * nums[j],
                             dp[i - 1][j] + left_right * nums[i])
                for k in range(j + 1, i):
                    theMax = max(theMax, left_right * nums[k] \
                                 + dp[k - 1][j] + dp[i][k + 1])
                dp[i][j] = theMax
        return dp[-1][0]


        # # TLE 33/70
        # nums = [elem for elem in nums if elem != 0]
        # cache = {}

        # def dfs(*nums):
        #     n = len(nums)
        #     if n < 2:
        #         return sum(nums)
        #     elif n == 2:
        #         return nums[0] * nums[1] + max(nums)
        #     if nums in cache:
        #         return cache[nums]
        #     ret = max(nums[0] * nums[1] + dfs(*nums[1:]),
        #               nums[-1] * nums[-2] + dfs(*nums[:-1]))
        #     for i in range(1, n - 1):
        #         ret = max(ret, nums[i] * nums[i - 1] * nums[i + 1]
        #                   + dfs(*(nums[:i] + nums[i+1:])))
        #     cache[nums] = ret
        #     return ret

        # return dfs(*nums)



#assert Solution().maxCoins([3, 1, 5, 8]) == 167
print(Solution().maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2]))
print(Solution().maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2,5,5]))
