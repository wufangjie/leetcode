from utils import memo


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # brute force
        @memo
        def dfs(target, *left):
            if left[-1] >= target:
                return True
            elif left[0] + left[1] >= target: # save a lot of time
                return False
            for i, select in enumerate(left):
                if not dfs(target - select, *(left[:i] + left[i+1:])):
                    return True
            return False

        theMax = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if theMax < desiredTotal:
            return False
        elif theMax == desiredTotal:
            return bool(maxChoosableInteger & 1)
        return dfs(desiredTotal, *list(range(1, maxChoosableInteger+1)))


        # # wrong answer
        # choosed = maxChoosableInteger
        # i, j = 1, maxChoosableInteger - 1
        # while choosed < desiredTotal:
        #     if choosed < desiredTotal <= choosed + i:
        #         return False
        #     choosed += i + j
        #     i += 1
        #     j -= 1
        # return True

# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.



import time
tic = time.time()
assert not Solution().canIWin(10, 40)
assert not Solution().canIWin(20, 210)
assert not Solution().canIWin(18, 188)
print(time.time() - tic)
