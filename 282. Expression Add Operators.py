from itertools import product


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # # TLE 3 / 20
        # n = len(num)
        # num_list = [''] * (2 * n - 1)
        # num_list[::2] = num
        # result = []
        # for ops in product(*([('+', '-', '*', '')] * (n - 1))):
        #     if num[0] == '0' and ops[0] == '':
        #         continue
        #     for i in range(n - 2):
        #         if ops[i] != '' and num[i+1] == '0' and ops[i+1] == '':
        #             break
        #     else:
        #         num_list[1::2] = ops
        #         test = ''.join(num_list)
        #         if eval(test) == target:
        #             result.append(test)
        # return result


# assert sorted(Solution().addOperators('123', 6)) == sorted(["1+2+3", "1*2*3"])
# assert sorted(Solution().addOperators('232', 8)) == sorted(["2*3+2", "2+3*2"])
# assert sorted(Solution().addOperators('105', 5)) == sorted(["1*0+5","10-5"])
# assert sorted(Solution().addOperators('00', 0)) == sorted(["0+0", "0-0", "0*0"])
# import time
# tic = time.time()
# #assert sorted(Solution().addOperators("3456237490", 9191)) == sorted([])
# print(sorted(Solution().addOperators("3456237498", 6768)))
# print(time.time() - tic)

sorted(Solution().addOperators("3456237498", 6768))


# eval too slow, but still faster than hand code basic eval use stack
