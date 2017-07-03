'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p1 = p2 = head
        count = 0
        while p1.next:
            p1 = p1.next
            count += 1

        k %= (count + 1)
        while count != k:
            p2 = p2.next
            count -= 1

        p1.next = head
        head = p2.next
        p2.next = None
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

    a = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
    result = Solution().rotateRight(a, 7)

    for p in result:
        print(p.val)
