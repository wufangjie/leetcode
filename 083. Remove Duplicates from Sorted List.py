'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p_pre = p_cur = head
        pre_val = None
        while p_cur:
            if p_cur.val != p_pre.val:
                p_pre.next = p_cur
                p_pre, p_cur = p_cur, p_cur.next
            else:
                p_cur = p_cur.next
        p_pre.next = None
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

    node = Node(1, Node(1, Node(3, Node(4, Node(4, Node(5))))))
    #node = Node(1, Node(1))
    for p in Solution().deleteDuplicates(node):
        print(p.val)
