class Solution(object):
    operator_dict = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: -(-x // y) if x * y < 0 else x // y}

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for elem in tokens:
            if elem in self.operator_dict:
                b, a = stack.pop(), stack.pop()
                stack.append(self.operator_dict[elem](a, b))
            else:
                stack.append(int(elem))
        return stack.pop()


if __name__ == '__main__':
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["18"]) == 18
    assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
