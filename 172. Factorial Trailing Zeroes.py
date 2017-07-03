class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

if __name__ == '__main__':
    assert Solution().trailingZeroes(99) == 22
    assert Solution().trailingZeroes(1808548329) == 452137076
