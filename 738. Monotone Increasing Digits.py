class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        times = 1
        theMax = 9
        while N:
            num = N % 10
            if num == 0:
                N = (N - 1) // 10
                result = times * 10 - 1
                theMax = 9
            else:
                if num > theMax:
                    result = times * num - 1
                    theMax = num - 1
                else:
                    theMax = num
                    result += times * theMax
                N //= 10
            times *= 10
        return result



print(Solution().monotoneIncreasingDigits(10), 9)
print(Solution().monotoneIncreasingDigits(1234), 1234)
print(Solution().monotoneIncreasingDigits(332), 299)
