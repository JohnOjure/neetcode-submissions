from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()
        complement = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for elem in s:

            if elem not in complement:
                stack.append(elem)

            else: #if elem is a closing parenthesis
                if not stack or stack[-1] != complement[elem]:
                    return False
                else:
                    stack.pop()

        return not stack
        