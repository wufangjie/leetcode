class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        count = []
        i = 0
        typ = s[i] == '0'
        while 1:
            j = s.find('1' if typ else '0', i + 1)
            if j == -1:
                count.append(len(s) - i)
                break
            count.append(j - i)
            i = j
            typ ^= 1

        n = len(count)
        return sum(min(count[i], count[i + 1]) for i in range(n - 1))



print(Solution().countBinarySubstrings("00110011"))
print(Solution().countBinarySubstrings("10101"))
