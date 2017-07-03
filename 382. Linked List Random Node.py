# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode

import random

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 1
        ret, p = self.head.val, self.head.next
        while p:
            if random.random() < 1. / count:
                ret = p.val
            p = p.next
            count += 1
        return ret



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
obj = Solution(ListNode(10, ListNode(100, ListNode(100, ListNode(20, ListNode(20, ListNode(100)))))))
from collections import Counter
print(Counter(obj.getRandom() for _ in range(100)))
