from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        freq = Counter(word)

        counts = sorted(freq.values(), reverse=True)

        ans = 0
        for i, f in enumerate(counts):
            pushes = (i // 8) + 1
            ans += f * pushes

        return ans