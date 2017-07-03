return_true = {4 ** i for i in range(16)}


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in return_true


# 3 的话 (素数) 可以用求余, 4 不行
