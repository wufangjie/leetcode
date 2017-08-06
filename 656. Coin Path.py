class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if A[-1] == -1:
            return []
        N = len(A)
        if B == 1:
            if -1 in A:
                return []
            else:
                return list(range(1, N + 1))

        inf = float('inf')
        path_from = [-1] * (N + 1)
        dp = [0] + [inf] * (B - 1)
        for i, elem in enumerate(A):
            if elem == -1:
                dp[i] = inf
            else:
                theMin = min(dp)
                if theMin == inf:
                    return []

                pre = None
                for j in range(B):
                    if dp[(i + j) % B] == theMin:
                        if pre is None or A[i - B + j] == 0:
                            pre = j
                            # if A[-1] == 0 and i + j + 1 >= N:
                            #     break

                path_from[i + 1] = i + 1 - B + pre
                dp[i % B] = theMin + elem

        ret = [N]
        while ret[-1] > 1:
            ret.append(path_from[ret[-1]])
        ret.reverse()
        return ret



# I just don't understand what the Pai mean, the position or Ai
# if position what the occasion we need to compare n and m
# if Ai how to explain (4), it should be [1,2,3,4,5,6,7,9]
assert Solution().cheapestJump([1,2,4,1,0,1,1,2], 2) == [1,2,4,5,6,8]
assert Solution().cheapestJump([1,2,4,1,0,0,1,1,2], 2) == [1,2,4,5,6,7,9]
assert Solution().cheapestJump([1,0,0,0,0,0,0,0,2], 2) == [1,2,3,4,5,6,7,8,9]
assert Solution().cheapestJump([1,0,0,0,0,0,0,0,0], 2) == [1,2,3,4,5,6,7,8,9] # (4)

# when I submit, it's locked
