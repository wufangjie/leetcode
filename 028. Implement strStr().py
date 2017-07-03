'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
def get_mov(sub):
    def get_i_mov(i, mov):
        j = mov[i - 1]
        while j != -1:
            if sub[i - 1] == sub[j]:
                mov[i] = j + 1
                break
            else:
                j = mov[j]
    n = len(sub)
    mov = [-1] + [0] * (n - 1)
    for i in range(2, n):
        get_i_mov(i, mov)
    # 进一步优化
    for i in range(1, n):
        if sub[i] == sub[mov[i]]:
            mov[i] = mov[mov[i]]
    return mov


def kmp(main, sub):
    mov = get_mov(sub)
    i = j = 0
    n = len(sub)
    while i < len(main) and j < n:
        if main[i] == sub[j]:
            i += 1
            j += 1
        else:
            if mov[j] == -1:
                i += 1
                j = 0
            else:
                j = mov[j]
        if j == n:
            return i - j
    return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return 0 if needle == '' else kmp(haystack, needle)
