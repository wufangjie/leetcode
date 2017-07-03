'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

from itertools import product

table = [['*'], ['*'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
         ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
         ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]


def comb(digits):
    for temp in product(*[table[int(i)] for i in digits]):
        yield ''.join(temp)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        else:
            return [x for x in comb(digits)]


if __name__ == '__main__':
    assert Solution().letterCombinations("") == []
    print(Solution().letterCombinations("23"))
