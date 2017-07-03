class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = self.get_tuple(a)
        br, bi = self.get_tuple(b)
        return '{}+{}i'.format(ar * br - ai * bi, ar * bi + ai * br)

    @staticmethod
    def get_tuple(a):
        ar, ai = a.split('+')
        ar, ai = int(ar), int(ai[:-1])
        return ar, ai
