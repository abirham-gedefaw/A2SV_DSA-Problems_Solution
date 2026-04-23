class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        start = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                start = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, len(nums) - 1
        end = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                end = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [start, end]