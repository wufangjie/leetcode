class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        sep = (k + 2) >> 1
        i1, i2 = 1, n
        ret = []
        if k & 1:
            while i1 < sep and i2 >= sep:
                ret.append(i2)
                ret.append(i1)
                i1 += 1
                i2 -= 1
        else:
            while i1 < sep and i2 >= sep:
                ret.append(i1)
                ret.append(i2)
                i1 += 1
                i2 -= 1

        if i1 < sep:
            ret.extend(range(i1, sep))
        if i2 >= sep:
            ret.extend(range(i2, sep - 1, -1))
        return ret


print(Solution().constructArray(15, 1))
print(abs(np.diff(np.array(Solution().constructArray(15, 2)))))
print(abs(np.diff(np.array(Solution().constructArray(15, 3)))))


# import numpy as np
# print(abs(np.diff(np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)))))
# print(abs(np.diff(np.array((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1)))))
# print(abs(np.diff(np.array((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 15)))))
# print(abs(np.diff(np.array((3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 15, 1)))))
# print(abs(np.diff(np.array((3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 2, 14, 1, 15)))))
# print(abs(np.diff(np.array((4, 5, 6, 7, 8, 9, 10, 11, 12, 3, 13, 2, 14, 1, 15)))))

# print(abs(np.diff(np.array((8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15)))))
