# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) >> 1
            r = guess(mid)
            if r == 0:
                return mid
            elif r == 1:
                lo = mid + 1
            else:
                hi = mid - 1
