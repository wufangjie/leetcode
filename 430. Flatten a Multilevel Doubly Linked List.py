class Solution:
    def flatten(self, head):
        if head is None:
            return None
        return self.flatten_rec(head)[0]

    def flatten_rec(self, node):
        right = node
        while right.prev:
            left = right.prev
            if left.child:
                cs, ce = self.flatten_rec(left.child)
                left.child = None
                left.next = cs
                cs.prev = left
                ce.next = right
                right.prev = ce
            right = left
        start = right

        left = node
        while True:
            right = left.next
            if left.child:
                cs, ce = self.flatten_rec(left.child)
                left.child = None
                left.next = cs
                cs.prev = left
                if right:
                    ce.next = right
                    right.prev = ce
                else:
                    return start, ce
            elif right is None:
                return start, left
            left = right


        # while node.prev is not None:
        #     node = node.prev

        # start = node
        # while True:
        #     right = node.next
        #     if node.child:
        #         cs, ce = self.flatten_rec(node.child)
        #         node.child = None
        #         node.next = cs
        #         cs.prev = node
        #         if right:
        #             ce.next = right
        #             right.prev = ce
        #         else:
        #             return start, ce
        #     if right is None:
        #         return start, node
        #     node = right
