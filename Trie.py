class TrieNode:
    def __init__(self,val=None):
        self.child = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode(w)
            node = node.child[w]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w in node.child:
                node = node.child[w]
                continue
            return False
        return True if node.end else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w in node.child:
                node = node.child[w]
                continue
            return False
        return True


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"),t.search("app"))
    print(t.startsWith("app"))
