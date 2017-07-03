from collections import deque


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        n = len(coins)
        flag, count = object(), 1
        visited = set()
        Q = deque([(amount, 0), (flag, count)])
        while Q:
            left, i = Q.popleft()
            if left is flag:
                if Q:
                    count += 1
                    Q.append((flag, count))
                else:
                    return -1
            else:
                for j in range(i, n):
                    if left == coins[j]:
                        return count
                    elif (left not in visited and left > coins[j]
                          and (j != n - 1 or left % coins[-1] == 0)):
                        Q.append((left - coins[j], j))
                visited.add(left)

    # TLE
    def coinChange2(self, coins, amount):
        coins = sorted(coins, reverse=True)
        n = len(coins)

        Q = deque([(amount, 0, 0)])
        while Q:
            left, i, count = Q.popleft()
            if i == n or left < 0 or (i+1 == n and left % coins[-1] != 0):
                continue
            if left == 0:
                return count
            else:
                Q.appendleft((left, i+1, count))
                Q.append((left-coins[i], i, count+1))
        return -1












import time

tic = time.time()
assert Solution().coinChange([3,7,405,436], 8839) == 25
assert Solution().coinChange([227,99,328,299,42,322], 9847) == 31
assert Solution().coinChange([438,86,218,138,358,152,129], 7656) == 19
print(time.time() - tic)

tic = time.time()
assert Solution().coinChange2([3,7,405,436], 8839) == 25
assert Solution().coinChange2([227,99,328,299,42,322], 9847) == 31
assert Solution().coinChange2([438,86,218,138,358,152,129], 7656) == 19
print(time.time() - tic)
