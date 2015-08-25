__author__ = 'cenk'

class Solution(object):
    solution = []
    def isPalindrome(self,text):
        i = 0
        k = len(text) - 1
        while i < (len(text) / 2):
            if text[i] != text[k]:
                return False
            k -= 1
            i += 1
        return True

    def generateCandidates(self,given,soFar):
        currentLen = sum([len(i) for i in soFar])
        maximumCandidate = len(given) - currentLen
        candidates = []
        for i in range(1,maximumCandidate+1):
            candidates.append(given[currentLen:currentLen+i])
        return candidates

    def isSolution(self,given,current):
        currentLen = sum([len(i) for i in current])
        if currentLen == len(given):
            return True
        else:
            return False

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.solution = []
        self.partitionHelper(s,[])
        return self.solution

    def partitionHelper(self,s,current):
        if self.isSolution(s,current):
            tmp = current[:]
            self.solution.append(tmp)

        candidates = self.generateCandidates(s,current)
        for i in candidates:
            if self.isPalindrome(i):
                current.append(i)
                self.partitionHelper(s,current)
                current.pop()

s = "aab"
sol = Solution()
print sol.partition("aab")