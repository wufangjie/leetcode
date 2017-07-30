class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 2
        while True:
            if n == 1:
                return count
            elif i ** 2 > n:
                return count + n
            while n % i == 0:
                n //= i
                count += i
            i += 1 if i == 2 else 2
