# import bisect
# import heapq


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def mergesort(lo, hi):
            if hi - lo < 2:
                return 0

            mid = (lo + hi) >> 1
            ret = mergesort(lo, mid) + mergesort(mid, hi)
            i, j = lo, mid

            while i < mid and j < hi:
                if nums[i] > (nums[j] << 1):
                    ret += hi - j
                    i += 1
                else:
                    j += 1

            i, j = 0, mid
            pre = nums[lo:mid]
            for k in range(lo, hi):
                if pre[i] >= nums[j]:
                    nums[k] = pre[i]
                    i += 1
                    if i == mid - lo:
                        break
                else:
                    nums[k] = nums[j]
                    j += 1
                    if j == hi:
                        nums[k+1:hi] = pre[i:]
                        break

            # nums[lo:hi] = heapq.merge(nums[lo:mid], nums[mid:hi], reverse=True)
            # python2 do not support reverse keyword
            return ret

        return mergesort(0, len(nums))


        # TLE 137/137
        # pre = []
        # count = 0
        # for elem in nums:
        #     i = bisect.bisect_right(pre, elem << 1)
        #     count += len(pre) - i
        #     if elem > 0:
        #         bisect.insort(pre, elem, hi=i)
        #     elif elem < 0:
        #         bisect.insort(pre, elem, lo=i)
        #     else:
        #         pre.insert(i, 0)
        # return count




assert Solution().reversePairs([1,3,2,3,1]) == 2
assert Solution().reversePairs([2,4,3,5,1]) == 3
import time
tic = time.time()
print(Solution().reversePairs(list(range(50000))))
print(Solution().reversePairs([1,3,2,3,1,3,1,7,5,4,3,6,7,8,9,0,2,1,-2,3,-5]))
print(time.time() - tic)




# # my god, AVL tree is slower than bisect, TLE when 136/137
# class AVLNode(object):
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.equal = 1
#         self.bigger = 0
#         self.left = left
#         self.right = right
#         self.factor = 0

#     __repr__ = __str__ = lambda self: '{}(val={}, equal={}, bigger={}, factor={})'.format(self.__class__.__name__, self.val, self.equal, self.bigger, self.factor)


# class AVLTree(object):
#     def __init__(self):
#         self.root = None

#     def search(self, val):
#         return self._search(val, self.root)

#     def _search(self, val, node):
#         if node is None:
#             return 0
#         elif node.val == val:
#             return node.bigger
#         elif node.val > val:
#             return node.equal + node.bigger + self._search(val, node.left)
#         else:
#             return self._search(val, node.right)

#     def insert(self, val):
#         if self.root is None:
#             self.root = AVLNode(val)
#         else:
#             self.root = self._insert(val, self.root)[0]

#     def _insert(self, val, node):
#         deeper = False
#         if node is None:
#             node = AVLNode(val)
#             deeper = True
#         elif node.val == val:
#             node.equal += 1
#         elif node.val > val:
#             node.left, deeped = self._insert(val, node.left)
#             if deeped:
#                 if node.factor == -1:
#                     node = self.rotate(node)
#                 else:
#                     node.factor -= 1
#                     if node.factor == -1:
#                         deeper = True
#         else:
#             node.bigger += 1
#             node.right, deeped = self._insert(val, node.right)
#             if deeped:
#                 if node.factor == 1:
#                     node = self.rotate(node)
#                 else:
#                     node.factor += 1
#                     if node.factor == 1:
#                         deeper = True
#         return node, deeper

#     def rotate(self, node):
#         if node.factor == 1:
#             right = node.right
#             if right.factor == 1:
#                 node.right = right.left
#                 right.left = node
#                 node.factor = right.factor = 0
#                 self.reget_bigger(node)
#                 return right
#             else:
#                 left = right.left
#                 node.right = left.left
#                 right.left = left.right
#                 left.left = node
#                 left.right = right

#                 node.factor = right.factor = 0
#                 if left.factor == 1:
#                     node.factor = -1
#                 elif left.factor == -1:
#                     right.factor = 1
#                 left.factor = 0

#                 self.reget_bigger(node)
#                 left.bigger += right.equal + right.bigger
#                 return left
#         elif node.factor == -1:
#             left = node.left
#             if left.factor == -1:
#                 node.left = left.right
#                 left.right = node
#                 node.factor = left.factor = 0
#                 left.bigger += node.equal + node.bigger
#                 return left
#             else:
#                 right = left.right
#                 node.left = right.right
#                 left.right = right.left
#                 right.left = left
#                 right.right = node

#                 node.factor = left.factor = 0
#                 if right.factor == 1:
#                     left.factor = -1
#                 elif right.factor == -1:
#                     node.factor = 1
#                 right.factor = 0

#                 self.reget_bigger(left)
#                 right.bigger += node.equal + node.bigger
#                 return right

#     def reget_bigger(self, node):
#         node.bigger = 0
#         p = node.right
#         while p:
#             node.bigger += p.equal + p.bigger
#             p = p.left


# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         tree = AVLTree()
#         count = 0
#         for elem in nums:
#             count += tree.search(elem << 1)
#             tree.insert(elem)
#         return count
