class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, step, move = n, 1, 0
        while left != 1:
            step *= 2
            left >>= 1
            if left == 1:
                break

            if not ((n - move) // step) & 1:
                move -= step
            step *= 2
            left >>= 1

        return step + move



assert Solution().lastRemaining(9) == 6
assert Solution().lastRemaining(99) == 56
assert Solution().lastRemaining(999) == 504
