import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        n = area
        factors = []
        f = 2
        while n != 1:
            if n % f == 0:
                n //= f
                factors.append(f)
            elif f == 2:
                f = 3
            else:
                f += 2
            if f ** 2 > n:
                factors.append(n)
                break

        if area == 1:
            return [1, 1]
        elif len(factors) == 1:
            return [factors[0], 1]

        factors.reverse()
        n = len(factors)
        sqrt = math.sqrt(area)
        def dfs(i, current, best):
            if i >= n or current >= sqrt:
                test = abs(current - area // current)
                if test < best[0]:
                    best[:] = test, current
            else:
                if current * factors[-1] > sqrt:
                    test = abs(current - area // current)
                    if test < best[0]:
                        best[:] = test, current

                dfs(i + 1, current, best)
                dfs(i + 1, current * factors[i], best)

        best = [area - 1, 1]
        dfs(1, factors[0], best)
        return sorted([best[1], area // best[1]], reverse=True)



# brute force (from sqrt(area to 1) is faster
print(Solution().constructRectangle(8896))
print(Solution().constructRectangle(120))
