class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.parent = list(range(len(edges) + 1))
        for u, v in edges:
            pu, pv = self.find(u), self.find(v)
            if pu == pv:
                return [u, v]
            self.parent[pv] = pu

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]



print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]), [2, 3])
print(Solution().findRedundantConnection([[2,3],[5,2],[1,5],[4,2],[4,1]]))


# NOTE: the description is changed and much clearer:
# not a rooted tree
# no duplicate edges, otherwise not connected (N vertices and N - 1 edges)
# no cycles (no self-loop)

# my original rooted tree solution is wrong, see 685. Redundant Connection II.py
