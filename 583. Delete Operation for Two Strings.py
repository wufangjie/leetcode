from utils import memo


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1), len(word2)

        @memo
        def dfs(i, j):
            if i == n1:
                return n2 - j
            elif j == n2:
                return n1 - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j + 1)) + 1

        return dfs(0, 0)



print(Solution().minDistance("sea", "eat"))
