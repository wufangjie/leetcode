def get_mov(sub):
    n = len(sub)
    mov = [-1] + [0] * (n - 1)
    for i in range(2, n):
        j = mov[i - 1]
        while j != -1:
            if sub[i - 1] == sub[j]:
                mov[i] = j + 1
                break
            else:
                j = mov[j]
    for i in range(1, n):
        if sub[i] == sub[mov[i]]:
            mov[i] = mov[mov[i]]
    return mov


def kmp(s):
    n = len(s)
    mov = get_mov(s[:(n >> 1)])
    i, j = n - 1, 0
    while j < i:
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            if mov[j] == -1:
                i -= 1
                j = 0
            else:
                j = mov[j]
    return (s[:2*j:-1] if i == j else s[:2*j-1:-1]) + s


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return kmp(s)
        # for i in range(len(s), 1, -1):
        #     mid = i >> 1
        #     if s[:mid] == s[i-1:i-mid-1:-1]:
        #         break
        # else:
        #     i = 1
        # return s[i:][::-1] + s

assert Solution().shortestPalindrome("") == ""
assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
assert Solution().shortestPalindrome("abcd") == "dcbabcd"
