from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        count = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
            count[a] += 1

        Q = [u for u, c in count.items() if c == 0]
        result = []
        while Q:
            u = Q.pop()
            result.append(u)
            for v in graph[u]:
                count[v] -= 1
                if count[v] == 0:
                    Q.append(v)
        return [] if sum(count.values()) else result



Solution().findOrder(2, [[1,0]])
