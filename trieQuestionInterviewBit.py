__author__ = 'cenk'


class TrieNode(object):
    children = []
    key = ''
    value = 0
    def __init__(self,key= 0,value = 0):
        """
        Initialize your data structure here.
        """
        self.children = []
        self.value = value
        self.key = key

class Trie(object):
    counter = 1
    root = None
    words = []
    def __init__(self):
        self.root = TrieNode()
        self.words = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        self.insertHelper(word,self.root)

    def insertHelper(self, word, node):
        if len(word) == 0:
            return

        lastLetter = False
        letter = word[0]

        if len(word) == 1:
            lastLetter = True

        for child in node.children:
            if child.key == letter:
                if lastLetter:
                    self.counter += 1
                    child.value = self.counter
                    self.insertHelper(word[1:],child)
                    return
                else:
                    self.insertHelper(word[1:],child)
                    return

        if lastLetter:
            self.counter += 1
            newNode = TrieNode(letter,self.counter)
            node.children.append(newNode)
            self.insertHelper(word[1:],newNode)
        else:
            newNode = TrieNode(letter)
            node.children.append(newNode)
            self.insertHelper(word[1:],newNode)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        result = self.searchHelper(word,self.root,0,0)

        return word[:result]

    def searchHelper(self, word, node,prefix,counter):
        if len(word) == 0:
            return False

        lastLetter = False
        letter = word[0]

        if len(word) == 1:
            lastLetter = True

        for child in node.children:
            if child.key == letter:
                counter += 1
                if lastLetter and child.value != 0:
                    return prefix
                else:
                    if len(node.children) > 1 and node != self.root:
                        prefix = counter
                        return self.searchHelper(word[1:],child,prefix,counter)
                    else:
                        return self.searchHelper(word[1:],child,prefix,counter)
        return False


# Your Trie object will be instantiated and called as such:

trie = Trie()
trie.insert("zebra")
trie.insert("dog")
trie.insert("duck")
trie.insert("dove")

print trie.search("dog")

# zebra = z
# dog = dog
# duck = du
# dove = dov