class Solution(object):
    finalSolution = []

    def generateParenthesis(self,num):
        self.finalSolution = []
        self.generateParenthesisHelper(num,"")
        return self.finalSolution

    def generateParenthesisHelper(self, num,parans):
        """
        :type n: int
        :rtype: List[str]
        """
        if len(parans) > (num * 2):
            return False
        if num == 0:
            return
        elif num == 1:
            self.finalSolution.append("()")
            return
    
        if self.isSolution(num,parans):
            if len(parans) == (num * 2):
                self.finalSolution.append(parans)
    
        candidates = self.generateCandidates(parans)
        for i in candidates:
            self.generateParenthesisHelper(num,parans + i)
    
        return
    
    def generateCandidates(self,parans):
        result = []
        if len(parans) == 0:
            result.append("(")
            return result
        else:
            result = ["(",")"]
            return result

    def isSolution(self,num,parans):
        stack = []
        if (num * 2) != len(parans):
            return False
    
        for i in parans:
            if i == "(":
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if top == ")":
                    return False
    
        if len(stack) != 0:
            return False
    
        return True


s = Solution()
print s.generateParenthesis(1)
print "\n"
print s.generateParenthesis(3)