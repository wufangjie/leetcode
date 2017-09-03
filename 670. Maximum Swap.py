class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        strNum = str(num)
        n = len(strNum)
        if n < 2:
            return num

        later_max, later_idx = strNum[-1], n - 1
        i1 = i2 = None
        for i in range(n - 2, -1, -1):
            if strNum[i] > later_max:
                later_max, later_idx = strNum[i], i
            elif strNum[i] < later_max:
                i1, i2 = i, later_idx

        if i1 is not None:
            return int(strNum[:i1] + strNum[i2] + strNum[i1+1:i2]
                       + strNum[i1] + strNum[i2+1:])
        return num

        # str's functions: rfind, rindex

        # strNum = str(num)
        # n = len(strNum)
        # if n < 2:
        #     return num

        # max_idx = [(strNum[-1], n - 1)]
        # for i in range(n - 2, 0, -1):
        #     if strNum[i] > max_idx[-1][0]:
        #         max_idx.append((strNum[i], i))
        #     else:
        #         max_idx.append(max_idx[-1])

        # for i in range(n - 1):
        #     c2, i2 = max_idx[n - 2 - i]
        #     if strNum[i] < c2:
        #         return int(strNum[:i] + c2 + strNum[i+1:i2]
        #                    + strNum[i] + strNum[i2+1:])
        # return num



print(Solution().maximumSwap(2736), 7236)
print(Solution().maximumSwap(9973), 9973)
