class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        left_closed = False
        stack = []
        try:
            for elem in preorder.split(','):
                if elem != '#':
                    if left_closed:
                        stack.pop()
                        left_closed = False
                    stack.append(elem)
                elif left_closed:
                    stack.pop()
                else:
                    left_closed = True
        except IndexError:
            return False
        return not bool(stack)



Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
