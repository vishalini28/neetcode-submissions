class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                # The first popped element is the right operand (b)
                # The second popped element is the left operand (a)
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Use float division and cast to int to truncate toward zero
                    stack.append(int(a / b))
            else:
                # If it's a number, convert to int and push to stack
                stack.append(int(token))
                
        return stack[0]
