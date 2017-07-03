class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        planted = ([-2]
                   + [i for i, v in enumerate(flowerbed) if v == 1]
                   + [len(flowerbed) + 1])
        for i in range(len(planted) - 1):
            if planted[i + 1] - planted[i] > 3: # test case not cover
                n -= (planted[i + 1] - planted[i] - 2) >> 1
                if n <= 0:
                    return True
        return False


assert not Solution().canPlaceFlowers([1,0,1,0,1,0,1], 0)
