__author__ = 'cenk'


class Solution(object):
    solutions = []
    final = False
    def generateCandidates(self,nums,current):
        s = set(nums)
        currentSet = set(current)
        candidates = s - currentSet
        return list(candidates)

    def findStartNums(self,n,k):
        nFac = [ 1,2,6,24,120,720,5040,40320,362880 ]
        treeStart = (k - 1) / nFac[n - 2]
        return treeStart

    def getPermutation(self,n,k):
        self.solutions = []
        nums = []
        nFac = [ 1,2,6,24,120,720,5040,40320,362880 ]
        for i in range(1,n+1):
            nums.append(i)

        startingNum = self.findStartNums(n,k)
        startingResult = nums[startingNum]
        startingResultList = [startingResult]
        counter = startingNum * nFac[n-2]

        result = self.permutationsHelper(nums,startingResultList,[counter],k)
        return self.solutions[0]

    def permutationsHelper(self,nums,current,counter,k):
        if self.final == True:
            return
        # is solution
        if len(current) == len(nums):
            tmp = "".join([str(i) for i in current])
            counter[0] += 1
            if counter[0] == k:
                self.solutions.append((counter[0],tmp))
                self.final = True
            return

        candidates = self.generateCandidates(nums,current)
        for i in candidates:
            current.append(i)
            self.permutationsHelper(nums,current,counter,k)
            current.pop()

s = Solution()

print s.getPermutation(4,23)
