class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 3:
            return num + 1

        str_num = bin(num)[2:]
        n = len(str_num)
        dp = [1, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        cdp = dp[:]
        for i in range(1, n):
            cdp[i] += cdp[i - 1]

        ret = cdp[n - 1]
        pre = 0

        for i in range(1, n):
            if str_num[i] == '1':
                if i - pre == 1:
                    return ret + dp[n - pre]
                ret += cdp[n - i - 1]
                pre = i
        return ret + 1


print(Solution().findIntegers(100), 34)
print(Solution().findIntegers(8), 6)
