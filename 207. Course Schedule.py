from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        count = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
            count[a] += 1

        Q = [u for u, c in count.items() if c == 0]
        while Q:
            u = Q.pop()
            for v in graph[u]:
                count[v] -= 1
                if count[v] == 0:
                    Q.append(v)
        return sum(count.values()) == 0



assert Solution().canFinish(2, [[0, 1]])
