class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}
        for a, b in zip(s, t):
            if a not in s_dict and b not in t_dict:
                s_dict[a] = b
                t_dict[b] = a
            elif s_dict.get(a) != b or t_dict.get(b) != a:
                return False
        return True
