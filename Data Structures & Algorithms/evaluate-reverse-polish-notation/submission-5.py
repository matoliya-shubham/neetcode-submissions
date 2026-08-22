class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # print(f'stack: {stack}')
            if tok in ['+','-','*','/']:
                if tok == '+':
                    a = stack.pop()
                    b = stack.pop()
                    sum = b + a
                    stack.append(sum)
                elif tok == '-':
                    a = stack.pop()
                    b = stack.pop()
                    sum = b - a
                    stack.append(sum)
                elif tok == '*':
                    a = stack.pop()
                    b = stack.pop()
                    sum = b * a
                    stack.append(sum)
                elif tok == '/':
                    a = stack.pop()
                    b = stack.pop()
                    sum = int(b / a)
                    stack.append(sum)
            else:
                stack.append(int(tok))
        return stack[-1]
