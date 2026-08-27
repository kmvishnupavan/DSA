class Solution:
    def lexGreaterPermutation(self, s, target):

        n = len(s)

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # Try changing the permutation from right to left
        for i in range(n - 1, -1, -1):

            temp = freq.copy()

            # Match target[0...i-1]
            possible = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if temp[c] == 0:
                    possible = False
                    break

                temp[c] -= 1

            if not possible:
                continue

            current = ord(target[i]) - ord('a')

            # Find smallest character greater than target[i]
            for c in range(current + 1, 26):

                if temp[c] > 0:

                    ans = ""

                    # Prefix same as target
                    for j in range(i):
                        ans += target[j]

                    # Put a greater character
                    ans += chr(c + ord('a'))
                    temp[c] -= 1

                    # Fill remaining characters in sorted order
                    for x in range(26):
                        while temp[x] > 0:
                            ans += chr(x + ord('a'))
                            temp[x] -= 1

                    return ans

        return ""