class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}

        for token in tokens:
            if token in operations:
                num1,num2 = stack.pop(), stack.pop()
                if token == "+":
                    num1 += num2
                elif token == "-":
                    num1 = num2-num1
                elif token == "*":
                    num1 *= num2
                else:
                    num1 = int(float(num2)/num1)
                stack.append(int(num1))
            else:
                stack.append(int(token))
        
        return stack[0]
                