'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

def isValidIP(s):
    if not s:
        return False
    elif s == '0':
        return True
    elif s[0] == '0':
        return False
    return int(s) <= 255


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        results = []
        for i in range(max(1, n - 9), min(4, n - 2)):
            for j in range(max(1, n - i - 6), min(4, n - i - 1)):
                for k in range(max(1, n - i - j - 3), min(4, n - i - j)):
                    temp = s[:i], s[i:i + j], s[i + j:i + j + k], s[i + j + k:]
                    if all(map(lambda x: isValidIP(x), temp)):
                        results.append('.'.join(temp))
        return results

if __name__ == '__main__':
    Solution().restoreIpAddresses("25525511135")
