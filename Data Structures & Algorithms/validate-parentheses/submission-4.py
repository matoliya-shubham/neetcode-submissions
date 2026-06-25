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
                if stack and ch == seq[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return not stack