'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while True:
            nxt, l_or_r = self.find_next(root, 'left')
            if nxt is None:
                return
            pre = root = nxt.__getattribute__(l_or_r)
            while True:
                if l_or_r == 'right':
                    nxt, l_or_r = self.find_next(nxt.next, 'left')
                else:
                    nxt, l_or_r = self.find_next(nxt, 'right')
                if nxt is None:
                    break
                pre.next = nxt.__getattribute__(l_or_r)
                pre = pre.next

    def find_next(self, parent, left_or_right):
        # python no tail recursion, so use loop
        while parent:
            if left_or_right == 'left' and parent.left:
                return parent, 'left'
            elif parent.right:
                return parent, 'right'
            else:
                parent = parent.next
                left_or_right = 'left'
        return None, None


if __name__ == '__main__':
    TreeLinkNode.__str__ = lambda x: str(x.val)
    TreeLinkNode.__repr__ = lambda x: str(x.val)
    a = TreeLinkNode(1)
    b = TreeLinkNode(2)
    c = TreeLinkNode(3)
    d = TreeLinkNode(4)
    e = TreeLinkNode(5)
    f = TreeLinkNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f


    # python's assign order
    class Test:
        def __init__(self, a=1):
            self.a = a

    t = t.a = 5
    t.a = t = 5
