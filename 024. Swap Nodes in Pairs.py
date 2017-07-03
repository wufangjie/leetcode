'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = p3 = ListNode('root')
        p3.next = head
        while True:
            try:
                p1 = p3.next
                p2 = p1.next

                p1.next = p2.next if p2 else None
                p2.next, p3.next = p1, p2
                p3 = p1
            except AttributeError:
                break
        return root.next


if __name__ == '__main__':
    def iter_node(node):
        while node:
            yield node
            node = node.next
    ListNode.__iter__ = iter_node

    class Node(ListNode):
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

    a = Node(2, Node(4, Node(6, Node(5, Node(7, Node(4, Node(1)))))))
    result = Solution().swapPairs(a)

    for p in result:
        print(p.val)
