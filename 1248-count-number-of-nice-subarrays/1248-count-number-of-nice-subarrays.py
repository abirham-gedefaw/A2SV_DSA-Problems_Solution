class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = Counter({0: 1})
        result = 0
        odd_count = 0
        for num in nums:
            odd_count += num & 1
            result += count[odd_count - k]
            count[odd_count] += 1
        return result
        