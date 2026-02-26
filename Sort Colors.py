# with the time complexity of o(n**2).

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j],nums[i]


# but the optimal approch is the duch flag alghortim with the time complexity of o(n).

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, current, right = 0, 0, len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
