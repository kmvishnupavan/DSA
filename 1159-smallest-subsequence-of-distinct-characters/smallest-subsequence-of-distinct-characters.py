class Solution:
    def smallestSubsequence(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        stack = []
        seen = set()

        for ch in s:
            freq[ch] -= 1

            if ch in seen:
                continue

            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)