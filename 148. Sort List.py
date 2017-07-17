class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = slow = fast = head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
                # 这题是参考的网上, 这种写法还是要慎重, 一不小心就会出错
                # 出错的例子如下
            else:
                tail.next, tail, h2 = h2, h2, h2.next

        tail.next = h1 or h2
        return dummy.next


# actually O(logn) space, not O(1)


from utils import ListNode
a = ListNode('a')
b = ListNode('b', a)
c = ListNode('c', b)
# a, b, c, c.next, b.next = b, c, a, b.next, a.next # 1
# from left to right, c.next's c is ('a')
c.next, b.next, a, b, c = b.next, a.next, b, c, a # 2

print(*map(lambda x: x.next, [a, b, c]), sep='\n')
# 1 show not all assignment happened together

# 1
# ListNode(val = a)
# None
# ListNode(val = a)

# 2
# None
# ListNode(val = a)
# None
