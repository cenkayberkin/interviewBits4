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
        result = self.searchHelper(word,self.root)
        return result

    def searchHelper(self, word, node):
        if len(word) == 0:
            return False

        lastLetter = False
        letter = word[0]

        if len(word) == 1:
            lastLetter = True

        for child in node.children:
            if child.key == letter:
                if lastLetter and child.value != 0:
                    return True
                else:
                    return self.searchHelper(word[1:],child)
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.startsWithHelper(prefix,self.root,prefix)

    def startsWithHelper(self,prefix,node,originalPrefix):
        if len(prefix) == 0:
            return False

        lastLetter = False
        letter = prefix[0]

        if len(prefix) == 1:
            lastLetter = True

        for child in node.children:
            if child.key == letter:
                if lastLetter:
                    # prefixList = list(originalPrefix)
                    # self.childrenWords(child, prefixList)
                    if self.childrenWords2(child):
                        return True
                    else:
                        return False
                else:
                    return self.startsWithHelper(prefix[1:],child,originalPrefix)
        return False

    def childrenWords2(self,node):
        if node.value != 0:
            return True

        if node.children == []:
            return False

        for child in node.children:
            if child.value != 0:
                return True

            if self.childrenWords2(child):
                return True

    def childrenWords(self,node,word = []):
        if node.children == []:
            return

        for child in node.children:
            word.append(child.key)

            if child.value != 0:
                tmp = "".join(word)
                self.words.append(tmp)

            self.childrenWords(child,word)
            word.pop()


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("yes")
trie.insert("yeah")
trie.insert("yesterday")

# file = open("words")
#
# for word in file:
#     w = word.strip().lower()
#     trie.insert(w)

# print trie.search("yes")
print trie.startsWith("yesterday")
