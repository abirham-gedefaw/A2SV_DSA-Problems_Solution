class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        res = n
        for i, start in enumerate(nums):
            end = start + n - 1
            idx = bisect_right(nums, end)
            uniquelen = idx - i
            res = min(res, n - uniquelen)
        return res

        