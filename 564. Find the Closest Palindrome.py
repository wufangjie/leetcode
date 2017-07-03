'''
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Note:

    The input n is a positive integer represented by string, whose length will not exceed 18.
    If there is a tie, return the smaller one as answer.

Subscribe to see which companies asked this question.

'''

## not including itself ##

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        ln = len(n)
        if ln == 1:
            return str(int(n) - 1)

        half = (ln - 1) >> 1

        if n[half] == '0' or n[half] == '9':
            mmm = n[half]
        else:
            mmm = ''

        for i in range(half, -1, -1):
            if not (n[i] == n[-i-1] == mmm):
                break

        if i == 0 and mmm != '9' and n[0] == '1' and n[-1] < '2':
            return '9' * (ln - 1)

        residual = 0
        for j in range(half + 1):
            residual /= 10. # leetcode use python2
            if j >= i:
                mid_str = None if (j + 1) << 1 > ln else n[j+1 : -j-1]
                final, residual = self.deal(
                    n[j], n[-j-1], mid_str, residual, mmm)
                if not residual:
                    result = n[:j] + final + n[:j][::-1]
                    break
            else:
                residual += int(n[j]) - int(n[-j-1])

        if result == n: # if itself
            if n[0] != mmm:
                i += 1

            if i == 0 and mmm == '9':
                return '1' + '0' * (ln - 1) + '1'

            if i < ln >> 1:
                if mmm == '9':
                    temp = n[:i-1] + str(int(n[i-1]) + 1)
                    return temp + '0' * (ln-i*2) + temp[::-1]
                elif mmm == '0':
                    temp = n[:i-1] + str(int(n[i-1]) - 1)
                    temp = temp + '9' * (ln-i*2) + temp[::-1]
                    if temp[0] == '0':
                        temp = temp[1:-1] + '9'
                    return temp

            if (1 + half) << 1 == ln:
                temp = str(int(n[:half+1]) - 1)
                return temp + temp[::-1]
            else:
                temp = 1 if n[half] == '0' else int(n[half]) - 1
                return n[:half] + str(temp) + n[half+1:]

        return result

    def deal(self, a, b, mid_str, residual, mmm):
        if mid_str is None: # only one character
            if residual < -0.5:
                a = str(int(a) + 1)
            elif residual >= 0.5:
                a = str(int(a) - 1)
            return a, 0

        # import pdb
        # pdb.set_trace()
        nn = len(mid_str)
        ia = int(a)
        temp = ia * 11
        real = int(a + b) - residual
        if (temp + 11 - real < real - temp) and (mmm == '9' or nn == 0):
            return str(ia + 1) + '0' * nn + str(ia + 1), 0
        elif (temp - real >= real - temp + 11) and (mmm != '9' or nn == 0):
            return str(ia - 1) + '9' * nn + str(ia - 1), 0
        return a + mid_str + a, residual + ia - int(b) if nn == 1 else 0


if __name__ == '__main__':
    f = Solution().nearestPalindromic
    assert f('1') == '0'
    assert f('9') == '8'
    assert f('10') == '9'
    assert f('11') == '9'
    assert f('88') == '77'
    assert f('199') == '202'
    assert f('9999') == '10001'
    assert f('11562') == '11611'
    assert f('11561') == '11511'
    assert f('19091') == '19191'
    assert f('19891') == '19791'
    assert f('1839380') == '1839381'
    assert f('1009001') == '1008001'
    assert f('10099001') == '10100101'
    assert f('123873133') == '123868321'
    assert f('1837722381') =='1837667381'
    assert f('1837722382') =='1837777381'
    assert f('12346') == '12321'
    assert f('1805170081') == '1805115081'
    assert f('1938943391') == '1938888391'
