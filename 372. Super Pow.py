class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if len(b) == 1 and b[0] == 0:
            return 1

        a %= 1337

        c = a
        dct = {1: c}
        for i in range(2, 1338):
            c *= a
            c %= 1337
            if c == a:
                break
            dct[i] = c

        den = len(dct)
        dct[0] = dct[i - 1]

        pre = 0
        for elem in b:
            pre = (pre * 10 + elem) % den

        return dct[pre]


print(Solution().superPow(13, [3, 9, 8, 3, 5, 2, 7, 8, 1, 0, 2, 4]))
