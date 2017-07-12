from utils import memo


@memo
def choose(n, k):
    num = 1
    for i in range(n, k, -1):
        num *= i
    for i in range(2, n - k + 1):
        num //= i
    return num


@memo
def max_p_t(p, t): # pig, times
    if p == 1:
        return t + 1
    if t == 1:
        return 2 ** p
    return sum(choose(p, q) * max_p_t(q, t - 1) for q in range(p + 1))


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets <= 1: # NOTE 1 rather 0
            return 0

        p = 1
        times = minutesToTest // minutesToDie
        while max_p_t(p, times) < buckets:
            p += 1
        return p


# ** THE BEST QUESTION I MET EVER **

# NOTE 1: one pig can drink n buckets one time

# NOTE 2: (if you understand NOTE 4, just skip this) no pig drink buckets should more than per pig drink buckets, since no pig will die

# NOTE 3: last step, for example 3 pig 1 times, + means drink, per line means a pig
# +++---      # ++++----
# -+++--  vs  # ++--++--
# --+++-      # +-+-+-+-

# NOTE 4: other step, more than 1 pig dead
# ++++----------------      # ++++----------------++--+++
# ----++++------------  vs  # ----++++------------++++--+
# --------++++--------      # --------++++----------+++++



print(Solution().poorPigs(1000, 15, 60))
