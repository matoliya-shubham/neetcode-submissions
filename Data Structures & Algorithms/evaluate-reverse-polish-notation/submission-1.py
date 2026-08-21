class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            # print(f'stack: {stack}')
            if tok in ['+','-','*','/']:
                if tok == '+':
                    sum = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(sum)
                elif tok == '-':
                    sum = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(sum)
                elif tok == '*':
                    sum = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(sum)
                elif tok == '/':
                    sum = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(sum)
            else:
                stack.append(int(tok))
        return stack[-1]
