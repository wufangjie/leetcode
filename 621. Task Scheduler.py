from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        theMax = max(count.values())
        return max(len(tasks), ((theMax - 1) * (n + 1)
                                + sum(v == theMax for v in count.values())))
