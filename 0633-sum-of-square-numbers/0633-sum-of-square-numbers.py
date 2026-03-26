class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            sum_squres = left**2 + right**2
            if sum_squres > c:
                right -= 1
            elif sum_squres < c:
                left += 1
            else:
                return True
        return False

        