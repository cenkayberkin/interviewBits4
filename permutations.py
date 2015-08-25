__author__ = 'cenk'

class Solution(object):
    solutions = []

    def generateCandidates(self,nums,current):
        s = set(nums)
        currentSet = set(current)
        candidates = s - currentSet
        return list(candidates)

    def permute(self,nums):
        self.solutions  = []

        self.permutationsHelper(nums,[])
        return self.solutions

    def permutationsHelper(self,nums,current):
        # is solution
        if len(current) == len(nums):
            # tmp = "".join([str(i) for i in current])
            tmp = current[:]
            self.solutions.append(tmp)
            return

        candidates = self.generateCandidates(nums,current)

        for i in candidates:
            current.append(i)
            self.permutationsHelper(nums,current)
            current.pop()

s = Solution()
a=  [0,1]
print s.permute(a)