class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        window_size = 2 * k + 1

        if window_size > n:
            return result
        curr_window_sum = sum(nums[: window_size])
        result[k] = curr_window_sum // window_size
        for i in range(k + 1, n - k):
            curr_window_sum = curr_window_sum - nums[i - k - 1] + nums[i + k]
            result[i] = curr_window_sum // window_size
        return result
        