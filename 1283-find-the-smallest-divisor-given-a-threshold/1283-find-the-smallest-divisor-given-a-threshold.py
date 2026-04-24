class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isDivisor(d):
            total = 0
            for i in nums:
                total += ceil(i/d)
            return total <= threshold
        
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if isDivisor(mid):
                right = mid
            else:
                left = mid + 1
        return right
        