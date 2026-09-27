class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        current = ""

        for ch in s:
            if ch == '(':
                stack.append(current)
                current = ""

            elif ch == ')':
                current = current[::-1]
                current = stack.pop() + current

            else:
                current += ch

        return current