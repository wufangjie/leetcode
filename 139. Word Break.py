# from functools import wraps


# def memo(func):
#     cache = {}
#     @wraps(func)
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     wrapper._cache = cache
#     return wrapper

# linear dp is too slow
        # @memo
        # def dp(sub):
        #     if sub in wordSet:
        #         return True
        #     for i in range(1, len(sub)):
        #         if dp(sub[:i]) and dp(sub[i:]):
        #             return True
        #     return False
        # return dp(s)


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        maxlen = len(s)
        matched_before_position = [0]
        for i in range(1, maxlen+1):
            for j in matched_before_position:
                if s[j:i] in wordSet:
                    matched_before_position.append(i)
                    break
        return matched_before_position[-1] == maxlen
