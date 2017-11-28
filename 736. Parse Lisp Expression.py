class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        self.scope = [{}]
        self.stack = [[None]]

        for elem in expression.split(' '):
            if elem == '(let':
                self.scope.append({})
                self.stack.append(['let'])
            elif elem == '(add':
                self.stack.append(['add'])
            elif elem == '(mult':
                self.stack.append(['mult'])
            elif elem.endswith(')'):
                if elem == '1)))))':
                    import pdb; pdb.set_trace()
                atom = elem.rstrip(')')
                self.append_val(atom)
                for _ in range(len(elem) - len(atom)):
                    temp = self.stack.pop()
                    if temp[0] == 'let':
                        if not isinstance(temp[-1], int):
                            temp[-1] = self.find_value(temp[-1])
                        self.stack[-1].append(temp[-1])
                        self.scope.pop()
                    elif temp[0] == 'add':
                        self.append_val(temp[1] + temp[2])
                    else:
                        self.append_val(temp[1] * temp[2])
            else:
                self.append_val(elem)
        return self.stack[0][-1]

    def append_val(self, elem):
        if elem == '': # NOTE: not elem is wrong, elem can be 0
            pass
        elif isinstance(elem, int) or elem[0] == '-' or ('0' <= elem[0] <= '9'):
            # NOTE: negative
            elem = int(elem)
            if self.stack[-1][0] == 'let' and self.stack[-1][-1] != 'let':
                self.scope[-1][self.stack[-1].pop()] = elem
            else:
                self.stack[-1].append(elem)
        else:
            if self.stack[-1][0] == 'let':
                if self.stack[-1][-1] == 'let':
                    self.stack[-1].append(elem)
                else:
                    self.scope[-1][self.stack[-1].pop()] = self.find_value(elem)
            else:
                self.stack[-1].append(self.find_value(elem))

    def find_value(self, key):
        for i in range(len(self.scope) - 1, -1, -1):
            if key in self.scope[i]:
                return self.scope[i][key]




# print(Solution().evaluate('(add 1 2)'),  3)
# print(Solution().evaluate('(mult 3 (add 2 3))'), 15)
# print(Solution().evaluate('(let x 2 (mult x 5))'), 10)
# print(Solution().evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))'), 14)
# print(Solution().evaluate('(let x 3 x 2 x)'), 2)
# print(Solution().evaluate('(let x 1 y 2 x (add x y) (add x y))'), 5)
# print(Solution().evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))'), 6)
# print(Solution().evaluate('(let a1 3 b2 (add a1 1) b2) '), 4)
# print(Solution().evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"), 6)
# print(Solution().evaluate("(let x (add 12 -7) (mult x x))"), 25)


print(Solution().evaluate("(let x0 -1 x1 3 x2 3 x3 2 x4 -4 x5 4 x6 -2 x7 -4 x8 -4 x9 -1 (mult (mult x9 x0) (mult (let x0 1 x4 -1 x8 2 (add -10 -8)) (add (add (add (mult (mult (mult (mult -5 (mult 1 1)) -10) -6) (add x5 (add x6 (add x9 (mult 1 1))))) (let x0 -3 x7 -2 (mult (add (mult (mult 1 1) -2) x0) (let x0 -5 x9 0 (add (mult 1 1) -10))))) (mult (add (let x0 -1 x8 3 (mult (mult (mult 1 1) (mult 1 1)) x7)) (mult (mult (mult (mult 1 1) (mult 1 1)) -5) (add -6 (mult (mult 1 1) x0)))) -7)) -7))))"))
