class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i in range(len(s)):
            alphabet_position = 26 - (ord(s[i]) - ord('a'))
            string_position = i + 1

            total += alphabet_position * string_position

        return total