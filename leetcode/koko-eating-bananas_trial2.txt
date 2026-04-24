class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if speed_works(mid):
                right = mid
            else:
                left = mid + 1
        return right    
        