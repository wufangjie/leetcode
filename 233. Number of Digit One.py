from utils import memo


@memo
def rec_full(n):
    if n < 2:
        return n
    else:
        return 10 * rec_full(n - 1) + 10 ** (n - 1)


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        str_n = str(n)
        ln = len(str_n)
        count = 0
        for i, c in enumerate(str_n, 1):
            if c != '0':
                count += int(c) * rec_full(ln - i)
                if c == '1':
                    count += int(str_n[i-1:]) - 10 ** (ln - i) + 1
                else:
                    count += 10 ** (ln - i)
        return count


assert Solution().countDigitOne(12313231) == 11772518


# @memo
# def rec_full(n):
#     if n == 1:
#         return 1
#     else:
#         return 10 * rec_full(n - 1) + 10 ** (n - 1)
