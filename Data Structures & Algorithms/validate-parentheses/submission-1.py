class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = len(stack)
        seq = {
            '(': ')',
            '{': '}',
            "[": ']'
        }
        for ch in s:
            if(len(stack) > 0 and stack[len(stack) - 1] in seq and seq[stack[len(stack) - 1]] == ch):
                stack.pop()
            else:
                stack.append(ch)
        #     print(stack)
        # print(f"final {stack}")
        return len(stack) == 0