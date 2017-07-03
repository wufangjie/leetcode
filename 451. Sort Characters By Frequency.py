from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dct = Counter(s)
        # return ''.join(sorted(s, key=lambda x: (dct[x], x), reverse=True))

        return ''.join([k * c for k, c in sorted(
            Counter(s).items(), key=lambda x: -x[1])])


print(Solution().frequencySort('tree'))
