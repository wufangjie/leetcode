class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = len(s)

        # acceleration -- from discuss
        if s == s[::-1]:
            return 0
        for i in range(1, maxlen):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        ############################################################

        mini = ([(i - 1, i + 1) for i in range(1, maxlen - 1)
                 if s[i - 1] == s[i + 1]]
                + [(i - 1, i) for i in range(1, maxlen) if s[i - 1] == s[i]])

        def _expand(lo, hi):
            while lo >= 0 and hi < maxlen:
                if s[lo] != s[hi]:
                    return lo + 1, hi - 1
                lo -= 1
                hi += 1
            else:
                return lo + 1, hi - 1

        span_dict = {(i+j)/2.: _expand(i, j) for i, j in mini}

        def min_cut_between(lo, hi):
            temp_span = []
            for k, (a, b) in span_dict.items():
                if lo < k < hi:
                    r = min(k - a, k - lo, b - k, hi - k)
                    temp_span.append((int(k - r), int(k + r)))

            if not temp_span:
                return hi - lo
            else:
                temp_span = sorted(temp_span, key=lambda x: (x[0], -x[1]))
                new_span = [temp_span[0]]

                for i in range(1, len(temp_span)):
                    if temp_span[i][1] > new_span[-1][1]:
                        if temp_span[i][0] > new_span[-1][1]:
                            # must cut
                            return (min_cut_between(lo, new_span[-1][1])
                                    + min_cut_between(temp_span[i][0], hi)
                                    + temp_span[i][0] - new_span[-1][1])
                        else:
                            new_span.append(temp_span[i])

                points = find_possible_cut_point(new_span, lo, hi)
                if points:
                    theMin = float('inf')
                    for p in points:
                        ml = min_cut_between(lo, p)
                        mr = min_cut_between(p+1, hi)
                        theMin = min(theMin, ml + mr + 1)
                    return theMin
                else:
                    return 0

        def find_possible_cut_point(new_span, lo, hi):
            points = []
            for a, b in new_span:
                if a != lo:
                    points.append(a - 1)
                if b != hi:
                    points.append(b)
            return points

        return min_cut_between(0, maxlen - 1)


if __name__ == '__main__':
    assert Solution().minCut('ababababababababababababccdebabababababababababababa') == 6
    assert Solution().minCut('abababababaghgabababababccdebabababababababababababa') == 6
    assert Solution().minCut("kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu") == 89
