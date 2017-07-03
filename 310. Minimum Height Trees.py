from collections import defaultdict
import heapq


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        G = defaultdict(set)
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)

        H = {}
        def dfs_get_height(u):
            H[u] = 0
            height = 1
            for v in G[u]:
                if v not in H:
                    height = max(height, dfs_get_height(v) + 1)
            H[u] = height
            return height

        u = edges[0][0]
        dfs_get_height(u)

        test = heapq.nlargest(2, [[H[v], v] for v in G[u]])
        if len(test) == 1:
            test.append((0, -1))

        while True:
            if test[0][0] == test[1][0]:
                return [u]
            elif test[0][0] - test[1][0] == 1:
                return [u, test[0][1]]
            u, lu = test[0][1], u
            test = heapq.nlargest(2, [
                (H[v], v) for v in G[u] if v != lu] + [(test[1][0] + 1, lu)])


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print(Solution().findMinHeightTrees(2, [[0, 1]]))
print(Solution().findMinHeightTrees(1, []))
