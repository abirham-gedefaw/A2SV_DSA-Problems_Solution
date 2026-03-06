class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = 1

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                n += 1   
            if n == 3:
                return nums[i]
        if n < 3:
            return nums[0]
        