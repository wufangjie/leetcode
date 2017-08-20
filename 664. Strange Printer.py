class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        inf = float('inf')
        dp = [[1]]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                dp[-1].append(1)
                dp.append(dp[-1])
            else:
                dp.append([0] * i + [1])
                poss = []
                for j in range(i):
                    if s[j] == s[i]:
                        if poss and poss[-1][1] == j - 1:
                            poss[-1][1] += 1
                        else:
                            poss.append([j, j])

                m = len(poss)
                poss.append([i, i, 0])
                poss.reverse()

                for j in range(m):
                    poss[j + 1].append(
                        min(dp[poss[k][0] - 1][poss[j + 1][1] + 1] + poss[k][2]
                            for k in range(j, -1, -1)))
                    # b, e = poss[j + 1]
                    # theMin = inf
                    # for k in range(j, -1, -1):
                    #     pb, pe, v = poss[k]
                    #     theMin = min(theMin, dp[pb - 1][e + 1] + v)
                    # poss[j + 1].append(theMin)

                dp[i][i - 1] = 2
                for j in range(i - 2, -1, -1):
                    theMin = inf
                    for b, e, v in poss:
                        if e < j:
                            break
                        theMin = min(
                            theMin, v + 1 + (dp[b - 1][j] if b - 1 >= j else 0))
                    dp[i][j] = theMin

        return dp[-1][0]

        # if not s:
        #     return 0

        # s2 = [s[0]] # compress consecutive characters seems not a good idea
        # for elem in s:
        #     if elem != s2[-1]:
        #         s2.append(elem)
        # s = s2

        # inf = float('inf')
        # dp = [[1]]
        # for i in range(1, len(s)):
        #     dp.append([0] * i + [1])
        #     poss = [[j] for j in range(i) if s[j] == s[i]]

        #     m = len(poss)
        #     poss.append([i, 0])
        #     poss.reverse()

        #     for j in range(m):
        #         poss[j + 1].append(
        #             min(dp[poss[k][0] - 1][poss[j + 1][0] + 1] + poss[k][-1]
        #                 for k in range(j, -1, -1)))

        #     dp[i][i - 1] = 2
        #     for j in range(i - 2, -1, -1):
        #         theMin = inf
        #         for p, v in poss:
        #             if p < j:
        #                 break
        #             theMin = min(
        #                 theMin, v + 1 + (dp[p - 1][j] if p - 1 >= j else 0))
        #         dp[i][j] = theMin

        # return dp[-1][0]



print(Solution().strangePrinter('bab'), 2)
print(Solution().strangePrinter("qrfzkqyrvhunkyq"), 12)
print(Solution().strangePrinter('aaacccbbbaaabbbcccaaa'), 4)

# poss (begin, end, the later (from begin) part's min turns combine or seperate)
'aaacccbbbaaabbbcccaaa'
'cccbbbaaabbbccc'
'bbbaaabbb'
'aaa'
