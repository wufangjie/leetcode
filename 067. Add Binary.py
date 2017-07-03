'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

from collections import deque

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a) - 1, len(b) - 1
        backward = 0
        result = deque()
        labels = ['0', '1']
        while la >= 0 or lb >= 0:
            va = 1 if la >= 0 and a[la] == '1' else 0
            vb = 1 if lb >= 0 and b[lb] == '1' else 0
            result.appendleft(labels[va ^ vb ^ backward])
            backward = (va + vb + backward) >> 1
            la -= 1
            lb -= 1
        if backward:
            result.appendleft('1')
        return ''.join(result)


if __name__ == '__main__':
    assert Solution().addBinary('11', '1') == '100'
