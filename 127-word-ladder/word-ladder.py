from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        patterns = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, level = q.popleft()

            if word == endWord:
                return level

            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]

                for nei in patterns[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level + 1))

                patterns[pattern] = []

        return 0