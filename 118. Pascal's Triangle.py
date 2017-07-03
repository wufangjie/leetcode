'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def next_rec(level):
            yield 1
            for i in range(len(level) - 1):
                yield level[i] + level[i + 1]
            yield 1

        def pascal(n):
            if n == 0:
                return []
            if n == 1:
                return [[1]]
            result = [[1]]
            for i in range(1, n):
                result.append(list(next_rec(result[-1])))
            return result

        return pascal(numRows)


if __name__ == '__main__':
    Solution().generate(5)
