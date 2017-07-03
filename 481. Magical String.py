from collections import deque


class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        Q = deque([2])
        v = 1
        count = 1
        for _ in range(2, n):
            elem = Q.popleft()
            if elem == 1:
                Q.append(v)
                count += 1
            else:
                Q.append(v)
                Q.append(v)
            v = 2 if v == 1 else 1
        return count
