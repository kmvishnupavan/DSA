class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = set()
        visited.add(s)

        while queue:
            next_queue = []

            for current in queue:
                if is_valid(current):
                    return [x for x in queue if is_valid(x)]

                for i in range(len(current)):
                    if current[i] != '(' and current[i] != ')':
                        continue

                    # Skip removing duplicate consecutive parentheses
                    if i > 0 and current[i] == current[i - 1]:
                        continue

                    next_string = current[:i] + current[i + 1:]

                    if next_string not in visited:
                        visited.add(next_string)
                        next_queue.append(next_string)

            queue = next_queue

        return [""]