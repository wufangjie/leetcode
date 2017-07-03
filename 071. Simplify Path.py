'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for elem in path.split('/'):
            if elem == '..':
                if stack:
                    stack.pop()
            elif elem not in {'.', ''}:
                stack.append(elem)
        return '/' + '/'.join(stack)
