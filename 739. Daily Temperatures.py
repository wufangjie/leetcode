class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(temperatures)
        stack = [(float('inf'), -1)]
        for i, t in enumerate(temperatures):
            while t > stack[-1][0]:
                _, p = stack.pop()
                ret[p] = i - p
            stack.append((t, i))
        return ret




print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
