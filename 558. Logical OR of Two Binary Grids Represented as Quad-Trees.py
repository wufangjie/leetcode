"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

def make_leaf(val):
    return Node(val, 1, None, None, None, None)


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        v, n = self.intersect_rec(quadTree1, quadTree2)
        return n or make_leaf(v)

    def intersect_rec(self, node1, node2):
        if node1.isLeaf:
            if node1.val == 1:
                return 1, node1
            return node2.val, node2
        if node2.isLeaf:
            if node2.val == 1:
                return 1, node2
            return node1.val, node1

        tlv, tln = self.intersect_rec(node1.topLeft, node2.topLeft)
        trv, trn = self.intersect_rec(node1.topRight, node2.topRight)
        blv, bln = self.intersect_rec(node1.bottomLeft, node2.bottomLeft)
        brv, brn = self.intersect_rec(node1.bottomRight, node2.bottomRight)

        val = 1
        if tlv == trv == blv == brv:
            if ((tln is None or tln.isLeaf)
                and (trn is None or trn.isLeaf)
                and (bln is None or bln.isLeaf)
                and (brn is None or brn.isLeaf)):
                return tlv, None
            val = tlv
        return val, Node(val, 0,
                         tln or make_leaf(tlv),
                         trn or make_leaf(trv),
                         bln or make_leaf(blv),
                         brn or make_leaf(brv))
