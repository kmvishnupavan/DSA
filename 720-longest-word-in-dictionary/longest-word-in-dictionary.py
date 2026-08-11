class Solution:
    def longestWord(self, words):
        wordset = set(words)
        ans = ""

        for word in words:
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                valid = True

                for i in range(1, len(word)):
                    if word[:i] not in wordset:
                        valid = False
                        break

                if valid:
                    ans = word

        return ans