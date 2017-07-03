from functools import wraps


def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper._cache = cache
    return wrapper


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        temp = [p[0]]
        for c in p[1:]:
            if c != '*' or temp[-1] != '*':
                temp.append(c)
        p = ''.join(temp)

        ls, lp = len(s), len(p)

        @memo
        def match_after(ii, jj):
            if lp - jj - p.count('*', jj) > ls - ii:
                return False

            while ii < ls and jj < lp:
                if p[jj] == '*':
                    for d in range(ls - ii + 1):
                        if match_after(ii + d, jj + 1):
                            return True
                    return False
                elif p[jj] != '?' and s[ii] != p[jj]:
                    return False
                ii += 1
                jj += 1
            if (jj == lp - 1 and p[jj] == '*') or (ii == ls and jj == lp):
                return True
            else:
                return False

        return match_after(0, 0)


if __name__ == '__main__':
    assert Solution().isMatch("", "") == True
    assert Solution().isMatch("a", "") == False
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("a", "*") == True
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", "?*") == True
    assert Solution().isMatch("aab", "c*a*b") == False
    assert Solution().isMatch('abefcdgiescdfimde', 'ab*cd?i*de')

    import time
    tic = time.time()
    Solution().isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa", "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")
    print(time.time() - tic)
