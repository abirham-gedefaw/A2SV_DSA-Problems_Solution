# The first code is just sorting list and iterate over the sorted list to get the target indices.
# But the time complexity is o(n**2) which is not optimal since there is another optimal approch.

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        result = []

        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        for i in range(size):
            if nums[i] == target:
                result.append(i)

        return result

# The optimal approch is the following code with time complexity of o(n).

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        result = []
        target_frequency = 0
        nums_below_target = 0

        for i in range(size):
            if nums[i] < target:
                nums_below_target += 1
            else:
                if nums[i] == target:
                    target_frequency += 1
                    
        total = nums_below_target + target_frequency
        for i in range( nums_below_target, total):
            result.append(i)
