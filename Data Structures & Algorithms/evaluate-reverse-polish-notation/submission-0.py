class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the two operands (right one first)
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # "/"
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                # It's a number
                stack.append(int(token))
        
        return stack[0]