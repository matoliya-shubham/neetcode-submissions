class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        res = [0] * len(temperatures)
        stack = []
        # compare each element with top element of stack 
        # stack will contain nly indecies fo elements
        # if temperatures[i] > stack[-1] --> res[stack[-1]] = i - stack[-1] (keep doing it till this condition remain true)
        # else -> push i in stack 
        # in last if stack is not empty then assign 0 fro each index in stack
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
