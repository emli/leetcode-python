#time : O(N)
#space : O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(')')
            elif bracket == '{':
                stack.append('}')
            elif bracket == '[':
                stack.append(']')
            elif len(stack) == 0 or stack.pop() != bracket:
                return False
        return len(stack) == 0