from utils import ListNode


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = 0
        p = root
        while p is not None:
            n += 1
            p = p.next

        step = n // k
        big = (n - step * k)
        ret = [root]
        p = root
        for s in [step + 1] * big + [step] * (k - big - 1):
            while s > 1:
                p = p.next
                s -= 1
            if s == 1:
                p2 = p.next
                p.next = None
                p = p2
                # p, p.next = p.next, None
                ret.append(p)
            else:
                ret.append(None)
        return ret

# root = ListNode(1, ListNode(2, ListNode(3)))
# ret = Solution().splitListToParts(root, 5)

# root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
# ret = Solution().splitListToParts(root, 3)
