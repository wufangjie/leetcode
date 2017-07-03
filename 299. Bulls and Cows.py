from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count_bull = 0
        cow_a, cow_b = defaultdict(int), defaultdict(int)
        for a, b in zip(secret, guess):
            if a == b:
                count_bull += 1
            else:
                cow_a[a] += 1
                cow_b[b] += 1
        count_cow = 0
        for k, v in cow_b.items():
            count_cow += min(v, cow_a[k])
        return '{}A{}B'.format(count_bull, count_cow)




assert Solution().getHint("1807", "7810") == "1A3B"
assert Solution().getHint("1123", "0111") == "1A1B"
assert Solution().getHint("1123", "4511") == "0A2B"
