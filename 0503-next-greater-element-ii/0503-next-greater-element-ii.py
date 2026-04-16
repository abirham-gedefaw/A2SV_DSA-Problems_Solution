class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            curr_index = i % n
            while stack and nums[curr_index] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[curr_index]
            if i < n:
                stack.append(curr_index)
        return result
        