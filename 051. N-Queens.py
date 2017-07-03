'''
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
'''

def n_queen(n):
    def check(selected, i, ns):
        for j, s in enumerate(selected):
            if abs(ns - j) == abs(i - s):
                return False
        return True

    def queen_rec(results=[], selected=[]):
        ns = len(selected)
        if ns == n:
            results.append(selected)
            return
        for i in set(range(n)).difference(selected):
            if check(selected, i, ns):
                queen_rec(results, selected + [i])

    results = []
    queen_rec(results)
    return results


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return [[('.' * i + 'Q' + '.' * (n - i -1)) for i in res]
                for res in n_queen(n)]


if __name__ == '__main__':
    Solution().solveNQueens(4)
