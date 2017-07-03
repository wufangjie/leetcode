from utils import ListNode

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nA = nB = 0

        p = headA
        while p:
            nA += 1
            p = p.next
        p = headB
        while p:
            nB += 1
            p = p.next

        while nA > nB:
            headA = headA.next
            nA -= 1
        while nB > nA:
            headB = headB.next
            nB -= 1

        while headA and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
