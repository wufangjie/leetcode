from utils import memo

@memo
def minCount(n):
    if n < 4:
        return n
    theMin = n - 1
    for i in range(2, int(n ** 0.5)+1):
        theMin = min(theMin, minCount(n - i ** 2))
    return theMin + 1


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return minCount(n)

        # 5868ms
        # psn = [i ** 2 for i in range(1, int(n ** 0.5)+1)]
        # count = list(range(n + 1))
        # for i in range(n):
        #     for p in psn:
        #         if i + p <= n:
        #             count[i + p] = min(count[i + p], count[i] + 1)
        #         else:
        #             psn.pop()
        #             break
        # return count[-1]

if __name__ == '__main__':
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2
    assert Solution().numSquares(16) == 1
