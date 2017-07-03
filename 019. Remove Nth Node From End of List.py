'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def _remove_rec(p):
            if p is None:
                return 0
            temp = _remove_rec(p.next)
            if isinstance(temp, int):
                if n == temp:
                    p.next = p.next.next
                    return p
                else:
                    return temp + 1
            return p

        if isinstance(_remove_rec(head), int):
            return head.next
        else:
            return head



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

    node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    for p in Solution().removeNthFromEnd(node, 1):
        print(p.val)
