class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        a = self.edge_2(p1, p2)
        if a == 0: ####
            return False
        if self.edge_2(p1, p3) != a:
            return False
        if self.edge_2(p1, p4) != 2 * a:
            return False
        return self.edge_2(p2, p4) == self.edge_2(p3, p4) == a

    @staticmethod
    def edge_2(p1, p2):
        return sum((a - b) ** 2 for a, b in zip(p1, p2))
        #return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
