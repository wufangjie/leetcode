class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """beat 5.7%"""
    def construct(self, grid):
        return self.construct_rec(grid, 0, 0, len(grid)).node()

    def construct_rec(self, grid, x0, y0, dd):
        if dd == 1:
            return ToBeNode(grid[y0][x0], None)

        d2 = dd >> 1
        tl = self.construct_rec(grid, x0, y0, d2)
        tr = self.construct_rec(grid, x0 + d2, y0, d2)
        bl = self.construct_rec(grid, x0, y0 + d2, d2)
        br = self.construct_rec(grid, x0 + d2, y0 + d2, d2)
        if tl or tr or bl or br:
            node = Node(1, 0, tl.node(), tr.node(), bl.node(), br.node())
            return ToBeNode(1, node)

        if tl.val == tr.val == bl.val == br.val:
            return ToBeNode(tl.val, None)
        node = Node(1, 0, tl.node(), tr.node(), bl.node(), br.node())
        return ToBeNode(1, node)


class ToBeNode:
    def __init__(self, val, node):
        self.val = val
        self._node = node

    def node(self):
        return self._node or Node(self.val, 1, None, None, None, None)

    def __bool__(self):
        return self._node is not None




def make_leaf(val):
    return Node(val, 1, None, None, None, None)

class Solution:
    """beat 94.8%"""
    def construct(self, grid):
        v, n = self.construct_rec(grid, 0, 0, len(grid))
        return n or make_leaf(v)

    def construct_rec(self, grid, x0, y0, dd):
        if dd == 1:
            return grid[y0][x0], None

        d2 = dd >> 1
        tlv, tln = self.construct_rec(grid, x0, y0, d2)
        trv, trn = self.construct_rec(grid, x0 + d2, y0, d2)
        blv, bln = self.construct_rec(grid, x0, y0 + d2, d2)
        brv, brn = self.construct_rec(grid, x0 + d2, y0 + d2, d2)
        if tln or trn or bln or brn:
            node = Node(1, 0,
                        tln or make_leaf(tlv),
                        trn or make_leaf(trv),
                        bln or make_leaf(blv),
                        brn or make_leaf(brv))
            return 1, node
        if tlv == trv == blv == brv:
            return tlv, None
        return 1, Node(1, 0,
                       tln or make_leaf(tlv),
                       trn or make_leaf(trv),
                       bln or make_leaf(blv),
                       brn or make_leaf(brv))


# res = Solution().construct([[0,1],[1,0]])
# from pprint import pprint


# res = Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
# pprint(res)
