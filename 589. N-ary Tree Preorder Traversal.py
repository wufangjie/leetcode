"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Node:
    def __init__(self, x):
        self.seq = [x]

    def append(self, x):
        self.seq.append(x)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root.val is None:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children is not None:
                stack.extend(node.children[::-1])
        return res

    def postorder(self, root: 'Node') -> List[int]:
        if root.val is None:
            return []

        stack = [root]
        res = []
        node = None # pre node
        while stack:
            if (stack[-1].children is not None
                and node != stack[-1].children[-1]):
                stack.extend(stack[-1].children[::-1])
            else:
                node = stack.pop()
                res.append(node.val)
        return res
