class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        """operators = ['+', '-', '/', '*']

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                operandStack.append(tokens[i]) 
            else:
                y = int(operandStack.pop())
                x = int(operandStack.pop())

                if tokens[i] == '+':
                    ans = x + y
                    operandStack.append(ans)
                elif tokens[i] == '-':
                    ans = x - y
                    operandStack.append(ans)
                elif tokens[i] == '/':
                    ans = int(float(x) / y)
                    operandStack.append(ans)
                elif tokens[i] == '*':
                    ans = x * y
                    operandStack.append(ans)"""
        
        for c in tokens:
            if c == '+':
                y = int(operandStack.pop())
                x = int(operandStack.pop())
                ans = x + y
                operandStack.append(ans)
            elif c == '-':
                y = int(operandStack.pop())
                x = int(operandStack.pop())
                ans = x - y
                operandStack.append(ans)
            elif c == '/':
                y = int(operandStack.pop())
                x = int(operandStack.pop())
                ans = int(float(x) / y)
                operandStack.append(ans)
            elif c == '*':
                y = int(operandStack.pop())
                x = int(operandStack.pop())
                ans = x * y
                operandStack.append(ans)
            else:
                operandStack.append(int(c))

        
        return operandStack[0]