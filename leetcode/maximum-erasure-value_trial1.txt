class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = Counter()
        maxi = float("-inf")
        window_sum = 0
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            counter[nums[right]] += 1
            while counter[nums[right]] > 1:
                window_sum -= nums[left]
                counter[nums[left]] -= 1
                left += 1
            maxi = max(maxi, window_sum)
        return maxi

        