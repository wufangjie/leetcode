class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        total = 8 ** K
        board = [[0] * N for i in range(N)]
        board2 = [[0] * N for i in range(N)]
        board2[r][c] = total

        while K:
            K -= 1
            board, board2 = board2, board
            for r in range(N):
                for c in range(N):
                    board2[r][c] = 0
                    for r2, c2 in ((r-2, c-1), (r-2, c+1),
                                   (r+2, c-1), (r+2, c+1),
                                   (r-1, c-2), (r-1, c+2),
                                   (r+1, c-2), (r+1, c+2)):

                        if 0 <= r2 < N and 0 <= c2 < N:
                            board2[r][c] += board[r2][c2]
                    board2[r][c] //= 8
        return sum(sum(row) for row in board2) / (total + 0.0)

        # # TLE
        # def dfs(k, r, c):
        #     if k == 0:
        #         return 1
        #     k -= 1
        #     ret = 0
        #     for r2, c2 in ((r-2, c-1), (r-2, c+1),
        #                    (r+2, c-1), (r+2, c+1),
        #                    (r-1, c-2), (r-1, c+2),
        #                    (r+1, c-2), (r+1, c+2)):
        #         if 0 <= r2 < N and 0 <= c2 < N:
        #             ret += dfs(k, r2, c2)
        #     return ret / 8.0
        # return dfs(K, r, c)


print(Solution().knightProbability(3, 2, 0, 0))
print(Solution().knightProbability(3, 1, 0, 0))

print(Solution().knightProbability(8, 30, 6, 4))
print(Solution().knightProbability(10, 13, 5, 3))
