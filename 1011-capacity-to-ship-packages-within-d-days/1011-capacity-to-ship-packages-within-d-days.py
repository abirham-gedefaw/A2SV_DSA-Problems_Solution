class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(c):
            current = 0
            day = 1
            for w in weights:
                if current + w > c:
                    current = 0
                    day += 1
                current += w
            return day <= days
        
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return right