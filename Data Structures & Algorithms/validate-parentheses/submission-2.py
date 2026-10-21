class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char in openBrackets.keys():
                stack.append(openBrackets[char])
            else:
                if not stack: return False
                if stack[-1] == char:
                    stack.pop()
                else:
                    return False
        return not stack