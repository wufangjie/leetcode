'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

def isScramble_rec(s1, s2):
    n = len(s1)
    if n < 4:
        return True
    for i in range(1, n):
        if sorted(s1[:i]) == sorted(s2[:i]):
            if (isScramble_rec(s1[:i], s2[:i]) and
                isScramble_rec(s1[i:], s2[i:])):
                return True
        if sorted(s1[:i]) == sorted(s2[-i:]):
            if (isScramble_rec(s1[:i], s2[-i:]) and
                isScramble_rec(s1[i:], s2[:-i])):
                return True
    return False



class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        return isScramble_rec(s1, s2)


if __name__ == '__main__':
    assert Solution().isScramble("hobobyrqd", "hbyorqdbo")
