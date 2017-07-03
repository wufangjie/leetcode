'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


class Solution(object):
    def largestRectangleArea_TLE(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        pre = {heights[0]: heights[0]}
        theMax = heights[0]
        for i in range(1, n):
            areas = {}
            the_smallest_taller = float('inf')
            for max_height, current_sum in pre.items():
                if heights[i] >= max_height:
                    if max_height > theMax / n:
                        areas[max_height] = current_sum + max_height
                else:
                    the_smallest_taller = min(the_smallest_taller, max_height)
            if the_smallest_taller == float('inf'):
                if heights[i] > theMax / (n - i):
                    areas[heights[i]] = heights[i]
            else:
                areas[heights[i]] = ((pre[the_smallest_taller] //
                                      the_smallest_taller + 1) * heights[i])
            pre = areas
            for val in pre.values():
                theMax = max(theMax, val)
        return theMax


    def largestRectangleArea_2n(self, heights):
        if not heights:
            return 0

        theMax = float('-inf')
        stack = [(theMax, -1)]
        for i, h in enumerate(heights):
            idx = i
            while stack[-1][0] >= h:
                hh, idx = stack.pop()
                theMax = max(theMax, (i - idx) * hh)
            stack.append((h, idx))

        i += 1
        while stack:
            hh, idx = stack.pop()
            theMax = max(theMax, (i - idx) * hh)
        return theMax


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        theMax = 0
        stack = [-1]
        for i, h in enumerate(heights):
            while stack[-1] >= 0 and heights[stack[-1]] >= h:
                theMax = max(theMax, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] >= 0:
            theMax = max(theMax, heights[stack.pop()] * (i - stack[-1]))
        return theMax

# class Node:
#     def __init__(self, val, left=None, right=None, left_nodes=0, right_nodes=0):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.left_nodes = left_nodes
#         self.right_nodes = right_nodes


# def insert(tree, h, seq):
#     if tree is None:
#         return Node(h)
#     if h <= tree.val:
#         return Node(h, tree, left_nodes=seq)
#     else:
#         tree.right = insert(tree.right, h, seq - tree.left_nodes - 1)
#         tree.right_nodes += 1
#         return tree

# parent = root = Node(-1)
# heights = list(range(20000))
# for i, h in enumerate(heights):
#     tree = root
#     while tree:
#         if h <= tree.val:
#             parent.right = Node(h, tree, left_nodes=i)
#             break
#         else:
#             i -= tree.left_nodes + 1
#             tree.right_nodes += 1
#             parent, tree = tree, tree.right
#     else:
#         parent.right = Node(h)


# tree = None
# for i, h in enumerate(heights):
#     tree = insert(tree, h, i)


# def max_rec(tree):
#     if tree is None:
#         return 0
#     return max(tree.val * (tree.left_nodes + tree.right_nodes + 1),
#                max_rec(tree.left), max_rec(tree.right))


if __name__ == '__main__':
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea(range(2000))
    heights = [4, 8, 0, 5, 7, 6, 7, 1, 4, 7, 4, 3, 7, 5, 4, 4, 2, 8, 5, 1, 3, 1, 3, 7, 6, 6, 1, 3, 2, 0, 4, 2, 0, 7, 6, 6, 0, 2, 4, 6, 3, 5, 3, 3, 6, 3, 2, 4, 1, 4]
    assert Solution().largestRectangleArea(heights) == Solution().largestRectangleArea_2n(heights)
