'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
'''

def max_rect_in_hist(heights):
    theMax = 0
    stack = [-1]
    for i, h in enumerate(heights):
        while stack[-1] >= 0 and heights[stack[-1]] >= h:
            theMax = max(theMax, heights[stack.pop()] * (i - stack[-1] - 1))
        stack.append(i)

    while stack[-1] >= 0:
        theMax = max(theMax, heights[stack.pop()] * (i - stack[-1]))
    return theMax


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0 for _ in range(n)]
        theMax = float('-inf')
        for i in range(len(matrix)):
            heights = [h + 1 if v == '1' else 0
                       for h, v in zip(heights, matrix[i])]
            theMax = max(theMax, max_rect_in_hist(heights))
        return theMax


if __name__ == '__main__':
    assert Solution().maximalRectangle(["10100","10111","11111","10010"]) == 6
