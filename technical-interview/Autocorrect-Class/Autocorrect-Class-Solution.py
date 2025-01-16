class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word: str, allow_mismatch: bool = True) -> bool:
        return self._search(self.root, word, 0, allow_mismatch)

    def _search(self, node: TrieNode, word: str, index: int, allow_mismatch: bool) -> bool:
        if index == len(word):
            return node.is_end and not allow_mismatch

        char = word[index]
        if char in node.children:
            if self._search(node.children[char], word, index + 1, allow_mismatch):
                return True

        if allow_mismatch:
            for child_char, child_node in node.children.items():
                if child_char != char:
                    if self._search(child_node, word, index + 1, False):
                        return True

        return False

class Autocorrect:
    def __init__(self, valid_words):
        self.trie = Trie()
        self.valid_words = valid_words
        for word in valid_words:
            self.trie.insert(word)

    def correct(self, word):
        if self.trie.search(word, allow_mismatch=False):
            return word
        for valid_word in self.valid_words:
            if self._is_one_mismatch(word, valid_word):
                return valid_word
        return word

    def _is_one_mismatch(self, word1, word2):
        if len(word1) != len(word2):
            return False
        mismatch_count = 0
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
        return mismatch_count == 1

valid = ["hello", "world", "foo", "bar", "baz"]
words = ['heklo', 'hekko', 'worl', 'worll', 'fo', 'ba', 'bazz']

def autoCorrect(valid, words):
    corrector = Autocorrect(valid)
    corrected_words = []
    for word in words:
        corrected_words.append(corrector.correct(word))
    return corrected_words

print(autoCorrect(valid, words))