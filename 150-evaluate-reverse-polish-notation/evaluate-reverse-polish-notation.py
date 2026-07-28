class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    sign = -1 if (a < 0) ^ (b < 0) else 1
                    stack.append(sign * (abs(a) // abs(b)))
            else:
                stack.append(int(token))

        return stack[-1]