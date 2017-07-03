from collections import deque

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # # the method use gcd I haven't think out


        # # bfs
        # if z > x + y:
        #     return False

        # if x > y:
        #     x, y = y, x

        # Q = deque([(0, 0), (x, 0), (y, 0)])
        # visited = set(Q)
        # while Q:
        #     a, b = Q.popleft()
        #     if a + b == z:
        #         return True
        #     if b == 0:
        #         poss = [(0, a), (x, y + a - x)]
        #     elif a == 0:
        #         poss = [(0, b + x) if b + x <= y else (b + x - y, y),
        #                 (x, b - x) if b > x else (b, 0)]
        #     else:
        #         poss = [(a, 0), (0, b)]
        #     for state in poss:
        #         if state not in visited:
        #             visited.add(state)
        #             Q.append(state)
        # return False


        # # dfs
        # if z > x + y:
        #     return False

        # if x > y:
        #     x, y = y, x

        # stack = [(x, 0), (y, 0), (0, 0)]
        # visited = set(stack)
        # while stack:
        #     a, b = stack.pop()
        #     if a + b == z:
        #         return True
        #     if b == 0:
        #         poss = [(0, a), (x, y + a - x)]
        #     elif a == 0:
        #         poss = [(0, b + x) if b + x <= y else (b + x - y, y),
        #                 (x, b - x) if b > x else (b, 0)]
        #     else:
        #         poss = [(a, 0), (0, b)]
        #     for state in poss:
        #         if state not in visited:
        #             visited.add(state)
        #             stack.append(state)
        # return False


        # # maximum recursion exceed
        # def rec(a, b):
        #     if a + b == z:
        #         return True

        #     if (a, b) in visited:
        #         return False
        #     else:
        #         visited.add((a, b))

        #     if a == 0 and b == 0:
        #         return rec(x, 0) or rec(0, y)
        #     elif a == 0:
        #         return ((rec(0, b + x) if b + x <= y else rec(b + x - y, y))
        #                 or (rec(x, b - x) if b > x else rec(b, 0)))
        #     elif b == 0:
        #         return rec(0, a) or rec(x, y + a - x)
        #     else:
        #         return rec(a, 0) or rec(0, b)

        # return rec(0, 0)


# either dfs or bfs is TLE in python
import time
tic = time.time()
assert Solution().canMeasureWater(3, 5, 4)
assert not Solution().canMeasureWater(2, 6, 5)
assert Solution().canMeasureWater(22003, 31237, 1)
assert Solution().canMeasureWater(22003, 31237, 31238)
assert Solution().canMeasureWater(22003, 31237, 0)
#temp = Solution().canMeasureWater(22003, 31237, 1)
print(time.time() - tic)
