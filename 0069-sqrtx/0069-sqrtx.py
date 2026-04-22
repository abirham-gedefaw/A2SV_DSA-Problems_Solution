class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if mid <= x // mid:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

        # the other more efficent code willbe as follow:
        if x == 0:
            return 0
        guess = x
        while guess*guess > x:
            guess = (guess + x // guess)//2
        return guess
            
          
        