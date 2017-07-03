class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        while lo <= hi:
            quarter = (3 * lo + hi) >> 2
            if quarter ** 2 == num:
                return True
            elif quarter ** 2 > num:
                hi = quarter - 1
            else:
                lo = quarter + 1
        return False


    #     num = self.divide(num, 2)
    #     if num is None:
    #         return False

    #     k = 3
    #     while True:
    #         if num == 1:
    #             return True
    #         if num is None or num < k ** 2:
    #             return False
    #         num = self.divide(num, k)
    #         k += 2

    # @staticmethod
    # def divide(num, k):
    #     count = 0
    #     while num % k == 0:
    #         count += 1
    #         num //= k

    #     if count & 1:
    #         return None
    #     else:
    #         return num


# boring, use binary search

for i in range(1, 27):
    print(i, Solution().isPerfectSquare(i))
