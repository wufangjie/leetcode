from utils import memo


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        @memo
        def rec(i, j):
            if j - i < 2:
                return max(nums[i], nums[j])
            else:
                return max(nums[i] + min(rec(i + 2, j), rec(i + 1, j - 1)),
                           nums[j] + min(rec(i, j - 2), rec(i + 1, j - 1)))
        return 2 * rec(0, len(nums) - 1) >= sum(nums)



assert not Solution().PredictTheWinner([1, 5, 2])
assert Solution().PredictTheWinner([1, 5, 233, 7])
assert Solution().PredictTheWinner([1, 1, 1])
import time
tic = time.time()
print(Solution().PredictTheWinner([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]))
print(time.time() - tic)
