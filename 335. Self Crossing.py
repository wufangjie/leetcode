class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        inf = float('inf')
        n = len(x)
        if n < 3:
            return False

        ruld = [0, 0, 0, 0] # right, up, left, down
        next_max = inf
        current = [-x[1], x[0]]

        for i, elem in enumerate(x[2:], 2):
            i %= 4
            if elem >= next_max:
                return True

            xy = 1 if i in {0, 2} else 0
            pn = 1 if i in {0, 3} else -1
            new = current[xy] + pn * elem

            if pn * new > pn * ruld[i - 3]:
                next_max = inf
            else:
                if next_max is inf and pn * new >= pn * ruld[i - 1]:
                    ruld[i - 2] = ruld[i]
                next_max = abs(ruld[i - 2] - current[xy ^ 1])
            ruld[i - 1], current[xy] = current[xy], new
        return False



assert Solution().isSelfCrossing([2, 1, 1, 2])
assert not Solution().isSelfCrossing([1, 2, 3, 4])
assert Solution().isSelfCrossing([1, 1, 1, 1])
assert not Solution().isSelfCrossing([3,3,4,2,2])
assert Solution().isSelfCrossing([1,1,2,1,1])
assert not Solution().isSelfCrossing([3,3,3,2,1,1])
