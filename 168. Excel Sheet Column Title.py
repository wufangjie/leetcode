class Solution(object):
    charmap = {i: chr(65 + i) for i in range(26)}
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = limit = 0
        den, cum = [1], [0]
        while limit < n:
            count += 1
            den.append(den[-1] * 26)
            cum.append(cum[-1] + den[-1])
            limit += den[-1]

        result = []
        n -= 1
        while count:
            count -= 1
            temp = (n - cum[count]) // den[count]
            result.append(self.charmap[temp])
            n -= (temp + 1) * den[count]

        return ''.join(result)



if __name__ == '__main__':
    assert Solution().convertToTitle(1) == 'A'
    assert Solution().convertToTitle(26) == 'Z'
    assert Solution().convertToTitle(27) == 'AA'
    assert Solution().convertToTitle(53) == 'BA'
    assert Solution().convertToTitle(536346) == 'ADMJR'
