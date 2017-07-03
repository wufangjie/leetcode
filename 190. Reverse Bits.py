class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{:0<32s}'.format(bin(n)[:1:-1]), 2)
