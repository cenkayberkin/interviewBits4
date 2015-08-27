class Solution(object):
    solutions = []

    def permuteUnique(self,nums):
        self.solutions = []
        testSeq = [i for i in range(len(nums))]
        self.permutationsHelper(testSeq,[])
        resultSet = set()

        for solution in self.solutions:
            tmp = []
            for i in solution:
                tmp.append(nums[i])
            resultSet.add(tuple(tmp))

        result = []
        for i in list(resultSet):
            l = [int(k) for k in i]
            result.append(l)

        return result

    def generateCandidates(self,nums,current):
        s = set(nums)
        currentSet = set(current)
        candidates = s - currentSet
        return list(candidates)

    def permutationsHelper(self,nums,current):
        # is solution
        if len(current) == len(nums):
            tmp = current[:]
            self.solutions.append(tmp)
            return

        candidates = self.generateCandidates(nums,current)

        for i in candidates:
            current.append(i)
            self.permutationsHelper(nums,current)
            current.pop()

s = Solution()
a=  [3,3,1,2,3,2,3,1]
print s.permuteUnique(a)
