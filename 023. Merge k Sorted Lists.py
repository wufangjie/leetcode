'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge2Lists(l1, l2):
    root = p = ListNode('root')
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return root.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge_rec(lists, lo, hi):
            if lo == hi:
                return lists[lo]
            else:
                mid = (lo + hi) >> 1
                return merge2Lists(merge_rec(lists, lo, mid),
                                   merge_rec(lists, mid + 1, hi))
        return [] if lists == [] else merge_rec(lists, 0, len(lists) - 1)


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

    a = Node(2, Node(4, Node(6)))
    b = Node(1, Node(9, Node(14)))
    c = Node(5, Node(7, Node(15, Node(25))))
    result = Solution().mergeKLists([a, b, c])

    for p in result:
        print(p.val)
