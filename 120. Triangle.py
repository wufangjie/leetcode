'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[0] + [float('inf')] * n
        for row in range(1, n):
            for col in range(row, -1, -1):
                dp[col] = min(dp[col - 1], dp[col]) + triangle[row][col]
        return min(dp)


if __name__ == '__main__':
    Solution().minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]])
