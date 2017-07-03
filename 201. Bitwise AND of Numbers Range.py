class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m

        m, n = bin(m)[2:], bin(n)[2:]
        length = len(n)
        if length == 1 or len(m) < length:
            return 0

        for i in range(length):
            if m[i] != n[i]:
                break
        return int(m[:i], 2) << (length - i)


if __name__ == '__main__':
    assert Solution().rangeBitwiseAnd(5, 7) == 4
    assert Solution().rangeBitwiseAnd(6, 7) == 6
    assert Solution().rangeBitwiseAnd(7, 7) == 7
    assert Solution().rangeBitwiseAnd(0, 1) == 0
