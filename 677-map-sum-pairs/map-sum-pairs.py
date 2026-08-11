class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.values = {}

    def insert(self, key, val):
        old_value = self.values.get(key, 0)
        diff = val - old_value

        self.values[key] = val

        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.sum += diff

    def sum(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return 0

            node = node.children[ch]

        return node.sum