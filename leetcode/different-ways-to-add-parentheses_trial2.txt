class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        elif char == '*':
                            res.append(l * r)
        if not res:
            res.append(int(expression))
        return res
