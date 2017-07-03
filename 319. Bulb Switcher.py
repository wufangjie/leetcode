class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # prime factor's power must even, ie perfact square
        return int(n ** (0.5))

        # states = [True] * n
        # for i in range(1, n):
        #     for j in range(i, n, i + 1):
        #         states[j] ^= True
        # return sum(states)


#print(Solution().bulbSwitch(999999))
