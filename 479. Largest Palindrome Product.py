from math import sqrt


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        if n & 1:
            sup = 10 ** (n - 1)
            sup10 = sup * 10
            for i in range(1, sup):
                temp = str(i)
                poss = sup10 ** 2 - int(
                    temp + temp[::-1] + '0' * (n - len(temp) - 1) + '1')
                for i in range(poss // sup10 + 1, min(int(sqrt(poss)) + 1, sup10)):
                    if poss % i == 0:
                        return poss % 1337
        else:
            n2 = n >> 1
            return int('9' * n2 + '0' * n + '9' * n2) % 1337
            #return int('9' * n) * int('9' * n2 + '0' * (n2 - 1) + '1') % 1337


import time
tic = time.time()
for i in range(1, 9):
    print(Solution().largestPalindrome(i))
print(time.time() - tic)


# 906609 924, 962
# 99000099 9999 9901
# 9966006699 99681 99979
# 999000000999 999999 999001
# 99956644665999 9997647 9998017
# 9999000000009999 99999999 99990001



# # brute force
# hi = 100000
# theMax = 0
# i = hi - 1
# while True:
#     prod = i ** 2
#     j = i
#     while True:
#         if prod <= theMax:
#             break
#         if prod % 10 == 9:
#             temp = str(prod)
#             if temp == temp[::-1]:
#                 theMax = prod
#                 break
#         prod -= i
#         j -= 1
#     if j == i:
#         break
#     i -= 1
# print(theMax)
