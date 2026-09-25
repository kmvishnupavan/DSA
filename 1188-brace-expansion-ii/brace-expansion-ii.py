class Solution(object):
    def braceExpansionII(self, expression):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)

                    temp = set()
                    for a in current:
                        for b in inside:
                            temp.add(a + b)

                    current = temp

                else:
                    temp = set()
                    for a in current:
                        temp.add(a + expression[i])

                    current = temp
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, i = parse(0)
        return sorted(result)