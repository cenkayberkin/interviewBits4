__author__ = 'cenk'


class Solution:
    def findPath(self,text,k):
        length = len(text)
        nFac = [ 1,2,6,24,120,720,5040,40320,362880 ]
        length -= 1
        path = (k - 1) / nFac[length - 1]
        newK = k - (path * nFac[length - 1])
        return path,newK

    def getPermutation(self,n,k):
        nums = [i for i in range(1,n+1)]
        result = ""
        newK  = k
        while len(nums) > 0:
            path,newK = self.findPath(nums,newK)
            result += str(nums[path])
            nums.remove(nums[path])
        return result

s = Solution()
print s.getPermutation(3,6)
# print findPath("1234",13)