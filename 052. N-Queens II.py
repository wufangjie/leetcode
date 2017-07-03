'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

def n_queen_count(n):
    def check(selected, i, ns):
        for j, s in enumerate(selected):
            if abs(ns - j) == abs(i - s):
                return False
        return True

    def queen_rec(count=[0], selected=[]):
        ns = len(selected)
        if ns == n:
            count[0] += 1
            return
        for i in set(range(n)).difference(selected):
            if check(selected, i, ns):
                queen_rec(count, selected + [i])

    count = [0]
    queen_rec(count)
    return count[0]


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n_queen_count(n)
