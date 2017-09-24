class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.parent = list(range(2001))
        for u, v in edges:
            pu, pv = self.find(u), self.find(v)
            if pu == pv:
                return [u, v]
            self.parent[pv] = pu

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]


    # NOTE: if the description is right (a rooted tree),
    # then it is not easy to solve the two root thing
    def findRedundantConnection2(self, edges):
        if len(edges) == 2:
            return edges[1]
        parent = {}
        for i, (u, v) in enumerate(edges):
            if v in parent:
                p0 = parent[v]
                if p0 in parent:
                    return [u, v]
                for u1, v1 in edges[i+1:]:
                    if v1 == p0:
                        return [u, v]
                if sum(1 for u1, v1 in edges if u1 == p0) == 1:
                    return [p0, v]
                else:
                    return [u, v]
            else:
                p = u
                while p in parent:
                    p = parent[p]
                    if p == v:
                        return [u, v]
                parent[v] = u




# print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]), [2, 3])
# print(Solution().findRedundantConnection([[2,3],[5,2],[1,5],[4,2],[4,1]]))


# assume not dumplicate
# NOTE:
# It seems like the description is wrong. # I think the answer is wrong
# need not to be a rooted tree, a child may have two parents, as follows:

# Input:[[2,3],[5,2],[1,5],[4,2],[4,1]]
# Output:[4,2]
# Expected:[4,1]


# NOTE2:
# assume the description is correct, then we must consider the two root thing:
[[1, 2], [3, 2], [4, 3]] # for example

print(Solution().findRedundantConnection2([[1,2], [1,3], [3,1]]), [3, 1])
print(Solution().findRedundantConnection2([[1, 2], [3, 2], [4, 3]]), [1, 2])
print(Solution().findRedundantConnection2([[1, 2], [2, 3], [4, 3], [4, 5], [1, 4]]), [4, 3])
