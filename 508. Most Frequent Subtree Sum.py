from utils import TreeNode
from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dct = defaultdict(int)
        def dfs(node):
            if node is None:
                return 0
            theSum = node.val + dfs(node.left) + dfs(node.right)
            dct[theSum] += 1
            return theSum
        dfs(root)
        theMax = max(dct.values())
        return [k for k, v in dct.items() if v == theMax]


# NOTE: **important** 不要把重复计算放到 comprehension 中, 跟平常的代码一样, 不会优化
dct = {i: i for i in range(1000)}
n = 10
import time
tic = time.time()
for _ in range(1000):
    d = [k for k, v in dct.items() if v == max(dct.values())]
print(time.time() - tic) # about 16.7s
tic = time.time()
for _ in range(1000):
    theMax = max(dct.values())
    d = [k for k, v in dct.items() if v == theMax]
print(time.time() - tic) # about 0.06s
