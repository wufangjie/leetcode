class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack_op = []
        stack_num = []

        op_dict = {'+': {'order': 1, 'func': lambda x, y: x + y},
                   '-': {'order': 1, 'func': lambda x, y: x - y},
                   '*': {'order': 2, 'func': lambda x, y: x * y},
                   '/': {'order': 2, 'func': lambda x, y: x // y}}

        num = []
        for c in s:
            if c == ' ':
                continue
            elif c in op_dict:
                if num:
                    stack_num.append(int(''.join(num)))
                    num = []

                order = op_dict[c]['order']
                while stack_op and op_dict[stack_op[-1]]['order'] >= order:
                    b, a = stack_num.pop(), stack_num.pop()
                    op = stack_op.pop()
                    stack_num.append(op_dict[op]['func'](a, b))
                stack_op.append(c)
            else:
                num.append(c)

        if num:
            stack_num.append(int(''.join(num)))
        while stack_op:
            b, a = stack_num.pop(), stack_num.pop()
            op = stack_op.pop()
            stack_num.append(op_dict[op]['func'](a, b))

        return stack_num[-1]
