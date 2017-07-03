class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        ret = 0
        while z:
            ret += z & 1
            z >>= 1
        return ret
