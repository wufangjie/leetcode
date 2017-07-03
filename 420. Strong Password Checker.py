from collections import deque


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 6

        n = len(s)
        lower = upper = digit = False
        repeat = []
        pre = 0
        for i, c in enumerate(s):
            if c != s[pre]:
                if i - pre > 2:
                    repeat.append(i - pre)
                pre = i
            if not lower and 'a' <= c <= 'z':
                lower = True
            if not upper and 'A' <= c <= 'Z':
                upper = True
            if not digit and '0' <= c <= '9':
                digit = True

        if i - pre > 1:
            repeat.append(i + 1 - pre)

        three = 3 - lower - upper - digit

        if n > 20:
            delete = n - 20
            repeat = deque(sorted(repeat, key=lambda x: x % 3))
            while repeat and delete:
                r = repeat.popleft()
                if r % 3 == 0:
                    delete -= 1
                    if r - 1 > 2:
                        repeat.append(r - 1)
                elif r % 3 == 1:
                    to_del = min(delete, 2)
                    delete -= to_del
                    if r - to_del > 2:
                        repeat.append(r - to_del)
                else:
                    to_del = min(delete, r - 2)
                    delete -= to_del
                    if r - to_del > 2:
                        repeat.append(r - to_del)
            return n - 20 + max(sum([r // 3 for r in repeat]), three)
        elif n >= 6:
            return max(sum([r // 3 for r in repeat]), three)
        else:
            return max(three, 6 - n)
        # elif n == 5:
        #     if three <= 1 and repeat and repeat[0] == 5: # never
        #         return 2
        #     else:
        #         return max(three, 1)
        # elif n == 4:
        #     return max(three, 2)
        # elif n < 4:
        #     return 6 - n



# print(Solution().strongPasswordChecker('aaaaaaaadddddddddddffffffffffffssssssssssss.....'))
# replace is always better than insert + delete
print(Solution().strongPasswordChecker("aaa111"))
