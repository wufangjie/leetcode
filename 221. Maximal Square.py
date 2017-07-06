class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        nrow, ncol = len(matrix), len(matrix[0])

        dp = [1 if i == '1' else 0 for i in matrix[0]]
        theMax = max(dp)
        for i in range(1, nrow):
            dp[0] = int(matrix[i][0])
            theMax = max(theMax, dp[0])
            for j in range(1, ncol):
                if matrix[i][j] == '1':
                    if dp[j-1] != dp[j]:
                        dp[j] = min(dp[j-1], dp[j]) + 1
                    elif matrix[i-dp[j]][j-dp[j]] == '1':
                        dp[j] += 1
                        theMax = max(theMax, dp[j])
                else:
                    dp[j] = 0
        return theMax ** 2



        # TLE
        # def rec(u, d, l, r):
        #     if d < u or r < l:
        #         return 0
        #     for i in range(u, d+1):
        #         for j in range(l, r+1):
        #             if matrix[i][j] == '0':
        #                 # print(i, j)
        #                 return max(min(i-u, r-l+1),
        #                            find_left_or_right(u, d, l, j-1, i+1),
        #                            find_left_or_right(u, d, j+1, r, i),
        #                            # rec(u, d, l, j-1, i+1),
        #                            # rec(u, d, j+1, r, i),
        #                            rec(i+1, d, l, r))
        #     return min(d-u, r-l) + 1

        # def find_left_or_right(u, d, l, r, i):
        #     while i <= d and i - u < r - l:
        #         for j in range(l, r+1):
        #             if matrix[i][j] == '0':
        #                 return i - u
        #         i += 1
        #     return r - l + 1

        # return rec(0, nrow-1, 0, ncol-1) ** 2


print(Solution().maximalSquare(["101001110","111000001","001100011","011001001","110110010","011111101","101110010","111010001","011110010","100111000"]))

print(Solution().maximalSquare(["000","000","111"]))
#Solution().maximalSquare(["10100","10111","11111","10010"])
print(Solution().maximalSquare(a))

a = \
['1111111111111101001111111100111011111111',
 '1111011011111111101101111101111111111111',
 '0111101011111101101101101111111111111111',
 '0101101011111111111101111111010110111111',
 '1111111111110111110110010111111111111111',
 '1111111110110101111111111101011111101111',
 '0110110101110011111111111111110111110101',
 '0111111111111100111111100110011011010101',
 '1111011110111111111011011011110101101011',
 '1111111110111111111101101101110111101111',
 '1110110011111111111100111111111111111111',
 '1011111110111101111001110111111111111111',
 '0110111111111111101111110111011111011111',
 '1111111111111111011111111111110111111011',
 '1111100111111110101100111111111111101111',
 '1111101111111110111111011111111111011111',
 '1111101111111111111111011001111110011111',
 '1111110111111111011111111111110111110111',
 '1011111111111111010111110010111110111111',
 '1111110011111111111110111111111111111011',
 '1111111111111111110111011111011111011011',
 '1100011011111111111111011111011111111111',
 '1111101011111111111101100101110011111111',
 '1110010111111111111011011110111101111101',
 '1111111111111101101111111111101111111111',
 '1111111011111101111011111111111110111111',
 '1110011111111110111011111111110111110111',
 '1111111111111100111111010111111111110111',
 '1111111111111111111111000111111111011101',
 '1111110111111111111111111101100111011011',
 '1111011011111101101101111110111111101111',
 '1111111111011111111111111111111111111111',
 '1111111111111111111111111111111111111111',
 '1100011111111110111111111111101111111011',
 '1111101111111101111010111111111111111111',
 '0111111111110011111111110101011011111111',
 '1011011111101111111111101111111111110011',
 '1010111111111111111111111111111110011111',
 '0111101111011111111111111111110111111111',
 '0111111011111111011101111011101111111111',
 '0111111111110101111011111101011001111011',
 '1111111111111011110111111101111111101110',
 '1111101111111100111111111110111111001111',
 '1101101111110101111101111111100111010100',
 '0110111111100111110010111110111011011101']