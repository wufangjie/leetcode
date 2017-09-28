class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = list(range(len(edges) + 1))
        u2 = v2 = None
        for u, v in edges:
            if parent[v] == v:
                parent[v] = u
            else:
                u2, v2 = u, v

        if u2 is None:
            return self.findRedundantConnection(edges)

        p = parent[v2]
        while p != parent[p]:
            if p == v2:
                return [parent[v2], v2]
            p = parent[p]
        return [u2, v2]

    def findRedundantConnection(self, edges):
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





# NOTE:
# according to the description, the two root thing (left a single vertex and a tree) is impossible
# I did not realize the cycle may come along with the two parent problem
# two different vertices means no self-loop


print(Solution().findRedundantDirectedConnection([[1,2], [1,3], [3,1]]), [3, 1])
print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [4, 3], [4, 5], [1, 4]]), [4, 3])
print(Solution().findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]), [4, 1])
