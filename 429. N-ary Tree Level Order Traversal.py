"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#from collections import deque
#from itertools import chain

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            queue_next = []
            for node in queue:
                queue_next.extend(node.children) # faster than chain
            queue = queue_next
        return res
