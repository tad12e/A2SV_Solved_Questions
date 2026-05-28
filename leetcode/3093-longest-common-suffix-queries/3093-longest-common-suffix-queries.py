class TrieNode:
    def __init__(self):
        self.child = {}
        self.idx = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # returns True if i is better than j
        def better(i, j):
            if j == -1:
                return True
            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return True
            if len(wordsContainer[i]) == len(wordsContainer[j]):
                return i < j
            return False

        # build trie using reversed words
        for i, word in enumerate(wordsContainer):
            node = root

            if better(i, node.idx):
                node.idx = i

            for ch in reversed(word):
                if ch not in node.child:
                    node.child[ch] = TrieNode()

                node = node.child[ch]

                if better(i, node.idx):
                    node.idx = i

        ans = []

        # process queries
        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.child:
                    break
                node = node.child[ch]

            ans.append(node.idx)

        return ans