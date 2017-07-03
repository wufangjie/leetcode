class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if A > E:
            A, B, C, D, E, F, G, H = E, F, G, H, A, B, C, D

        test = min(D, H) - max(B, F)
        if test > 0:
            if C >= G:
                area -= test * (G - E)
            elif C > E:
                area -= test * (C - E)
        return area
