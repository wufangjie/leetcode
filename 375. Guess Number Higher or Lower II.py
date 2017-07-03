from utils import memo


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp0 = [0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 21]
        i0 = len(dp0)
        dp[:i0] = dp0

        step = 2
        for i in range(i0, n + 1):
            gss = i - 2 ** step + 1
            theMax = sum([i - 2 ** j + 1 for j in range(1, step)])
            if dp[gss - 1] > theMax:
                gss2 = gss - 2 ** step
                if theMax + gss2 < dp[gss - 1]:
                    step += 1
                    # print('----', i, step)
                    theMax += gss2
                else:
                    theMax = dp[gss - 1]
                    x = gss

                    for p in range(3, step):
                        left = 2 ** p
                        #step, left
                        theSum = x - left
                        j = 2 ** (step - 1)
                        base = x
                        while True:
                            if j >= left:
                                theSum += x + j
                            elif j * 2 == left:
                                # theSum += x
                                pass # not add gss for compare
                            else:
                                base += 2 * j
                                theSum += base
                            if j == 1:
                                break
                            j /= 2


                        if dp[x - left - 1] - left <= theSum:
                            #dp[x - left - 1] + x - left <= theSum + x:
                            theMax = min(theMax, theSum)
                            break
                        else:
                            theMax = min(theMax, dp[x - left - 1] - left)

                    # temp = sum([gss + 2 ** (step - 1) - 2 ** j
                    #             for j in range(1, step)]) + gss
                    # if dp[gss - 1] > temp:
                    #     t = gss - 2 ** (step - 1)
                    #     if dp[t - 1] + t < temp + gss:
                    #         print('----', i)

                    # theMax = min(dp[gss - 1],
                    #              sum([gss + 2 ** (step - 1) - 2 ** j
                    #                   for j in range(1, step)]) + gss)
            dp[i] = theMax + gss
        return dp[-1]


    def getMoneyAmount2(self, n):
        result = []
        @memo
        def dfs(l, r):
            if l >= r:
                return 0
            res = float('inf')
            for x in range((l + r) // 2, r + 1):
                res = min(res, x + max(dfs(l, x - 1), dfs(x + 1, r)))
            return res
        return dfs(1, n)


    # def getMoneyAmount2(self, n):
    #     memo={}
    #     def dfs(l, r):
    #         if l>=r:
    #             return 0
    #         elif (l,r) in memo:
    #             return memo[(l,r)]
    #         res=float('inf')
    #         for x in xrange((l+r)/2, r+1):
    #             res=min(res, x+ max(dfs(l, x-1), dfs(x+1, r))  )
    #         memo[(l,r)]=res
    #         return res
    #     return dfs(1, n)

        # step = [1]
        # for i in range(i0, n + 1):
        #     theSum = sum(step)
        #     gss = i - theSum - step[-1] * 2
        #     theMax = i * len(step) - theSum
        #     if i == 21:
        #         import pdb
        #         pdb.set_trace()
        #     if dp[gss - 1] > theMax:
        #         gss2 = gss - step[-1] * 4
        #         if theMax + gss2 < dp[gss - 1]:
        #             step.append(step[-1] * 2)
        #             theMax += gss2
        #         else:
        #             theMax = dp[gss - 1]
        #             #gss2 = gss - step
        #     dp[i] = theMax + gss
        # print(step)
        # return dp




        # for i in range(i0, n + 1):
        #     j = i
        #     theMin = (i - 1) + dp[i - 2]
        #     step = 2
        #     pre = 0
        #     while pre <= dp[j - 2]:
        #         pre += j - 1
        #         j -= step
        #         step *= 2
        #         # if i == 124:
        #         #      print(j - 1)
        #         theMin = min(theMin, max(pre + (j - 1), (j - 1) + dp[j - 2]))
        #     dp[i] = theMin
        # return dp


# move left 2,  x-2, ..., x+16, x+8, x+4, x+2, x
# move left 4,  x-4, ..., x+16, x+8, x+4, x, x+2
# move left 8,  x-8, ..., x+16, x+8, x, x+4, x+6
# move left 16,  x-16, ..., x+16, x, x+8, x+12, x+14
# move left 12,  x-12, ..., x+16, x, (later same as 16, if this worse than 16)

# x, left = 253, 8
# theSum = x - left
# j = 16
# base = x
# while True:
#     if j >= left:
#         theSum += x + j
#     elif j * 2 == left:
#         theSum += x
#     else:
#         base += 2 * j
#         theSum += base
#     if j == 1:
#         break
#     j /= 2
# print(theSum)

############# 其实右边也可以加, 不考虑了

assert Solution().getMoneyAmount(2100) == 16276
assert Solution().getMoneyAmount(810) == 5370
assert Solution().getMoneyAmount(284) == 1544
# 284
# for n in range(210, 298):
#     if Solution().getMoneyAmount(n) != Solution().getMoneyAmount2(n):
#         break


print(Solution().getMoneyAmount(284))

[0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 30, 34, 38, 42, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 86, 90, 94, 98, 102, 106, 110, 114, 119, 124, 129, 134, 139, 144, 149, 154, 160, 166, 172, 178, 182, 186, 190, 194, 198, 202, 206, 210, 214, 218, 222, 226, 230, 234, 238, 242, 246, 250, 254, 258, 262, 266, 270, 274, 278, 282, 286, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 376, 382, 388, 394, 400, 406, 412, 418, 424, 430, 436, 442, 448, 454, 460, 466, 473, 480, 487, 494, 501, 508, 515, 522, 529, 536, 543, 550, 557]
[0, 0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 30, 34, 38, 42, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 86, 90, 94, 98, 102, 106, 110, 114, 119, 124, 129, 134, 139, 144, 149, 154, 160, 166, 172, 178, 182, 186, 190, 194, 198, 202, 206, 210, 214, 218, 222, 226, 230, 234, 238, 242, 246, 250, 254, 258, 262, 266, 270, 274, 278, 282, 286, 290, 258, 262, 266, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 358, 362, 366, 370, 374, 378, 382, 386, 390, 394, 398, 402, 370, 374, 378, 382, 386, 390, 396, 402, 408, 414, 420, 426, 455, 460, 465, 470, 475]

# print(Solution().getMoneyAmount(124))
# dct = dict(zip(range(124), Solution().getMoneyAmount(124)))
# dct = dict(zip(range(284), Solution().getMoneyAmount(284)))

# assert Solution().getMoneyAmount(124) == 555
# 二分法不全正确, 有可能左边比右边多一层
# 101, 117, 109, 113, 115


# 102,103,104,105,106,107,108,109,110,111,112,113,114,115,116
# 118,119,120,121,122,123,124


# NOTE: the correct one need not pay
# first do it by hand
[[1, 0],
 [2, 1], # [1]
 [3, 2], # [2]
 [4, 4], # [3, 1]
 [5, 6], # [2, 4] or [4, 2]
 [6, 8], # [3, 5]
 [7, 10], # [4, 6]
 [8, 12], # [5, 7]
 [9, 14], # [6, 8]
 [10, 16], # [7, 9]
 [11, 18], # [8, 10]
 [12, 21], # [9] + [1 -> 8]
 [13, 24], # [10] + [1 -> 9]
 [14, 27], # [11] + [1 -> 10]
 [15, 30], # [12] + [1 -> 11]
 [16, 34], # [12] + [1 -> 11]
]
