class Solution(object):
    def evaluate(self, s, knowledge):
        mp = {}

        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = []

                while s[i] != ')':
                    key.append(s[i])
                    i += 1

                key = ''.join(key)

                if key in mp:
                    result.append(mp[key])
                else:
                    result.append('?')

                i += 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)