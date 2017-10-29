# from utils import memo



class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        nA, nB = len(A), len(B)
        theMax = 0
        dp = [0] * (nB + 1)
        for i in range(nA):
            for j in range(nB - 1, -1, -1):
                if A[i] == B[j]:
                    dp[j] = dp[j - 1] + 1
                    if dp[j] > theMax:
                        theMax = dp[j]
                else:
                    dp[j] = 0
        return theMax

        # # TLE
        # nA, nB = len(A), len(B)
        # theMax = 0

        # stack = [(0, 0, 0)]
        # while stack:
        #     i, j, acc = stack.pop()
        #     if i == nA or j == nB or acc + min((nA - i), (nB - j)) < theMax:
        #         continue
        #     stack.append((i + 1, j, 0))
        #     stack.append((i, j + 1, 0))
        #     if A[i] == B[j]:
        #         acc += 1
        #         if acc > theMax:
        #             theMax = acc
        #         stack.append((i + 1, j + 1, acc))
        # return theMax


        # # TLE
        # nA, nB = len(A), len(B)
        # theMax = [0]

        # _cache = set()

        # def dfs(i, j, acc):
        #     if i == nA or j == nB:
        #         return
        #     elif acc + min((nA - i), (nB - j)) < theMax[0]:
        #         return
        #     if (i, j) in _cache:
        #         return
        #     _cache.add((i, j))

        #     if A[i] == B[j]:
        #         acc += 1
        #         if acc > theMax[0]:
        #             theMax[0] = acc
        #         dfs(i + 1, j + 1, acc)

        #     dfs(i + 1, j, 0)
        #     dfs(i, j + 1, 0)

        # dfs(0, 0, 0)
        # return theMax[0]


print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))

print(Solution().findLength([0] * 1000, [0] * 1000))


print(Solution().findLength([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]))
