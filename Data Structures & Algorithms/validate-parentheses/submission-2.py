class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2 != 0):
            return False
        stack = []
        seq = {
            '(': ')',
            '{': '}',
            "[": ']'
        }
        for ch in s:
            if ch in seq:
                stack.append(ch)
            else:
                if len(stack) > 0 and ch == seq[stack[-1]]:
                    stack.pop()
                else:
                    return False
            # print(f"stack is {stack}")

        return len(stack) == 0