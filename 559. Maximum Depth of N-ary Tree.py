# from itertools import chain

# class Solution:
#     # 56ms, beat 20.48%
#     def maxDepth(self, root: 'Node') -> int:
#         if root is None:
#             return 0
#         count = 0
#         queue = [root]
#         while queue:
#             queue = list(chain(*(node.children for node in queue)))
#             count += 1
#         return count


class Solution:
    # 51ms, beat 46.12%
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        count = 0
        queue = [root]
        while queue:
            next_level = []
            for node in queue:
                next_level.extend(node.children)
            queue = next_level
            count += 1
        return count


# class Solution:
#     # 56ms, beat 20.48%
#     def maxDepth(self, root: 'Node') -> int:
#         if root is None:
#             return 0
#         stack = [(0, root)]
#         d_max = 0
#         while stack:
#             d, node = stack.pop()
#             d += 1
#             for child in node.children:
#                 stack.append((d, child))
#             d_max = max(d_max, d)
#         return d_max


# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


print(Solution().maxDepth(Node(0, [Node(i, []) for i in range(10)])))
