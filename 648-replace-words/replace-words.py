class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()

        # Build Trie
        for word in dictionary:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.isEnd = True

        # Find shortest root for each word
        def findRoot(word):
            node = root

            for i, ch in enumerate(word):
                if ch not in node.children:
                    return word

                node = node.children[ch]

                if node.isEnd:
                    return word[:i + 1]

            return word

        words = sentence.split()

        return " ".join(findRoot(word) for word in words)