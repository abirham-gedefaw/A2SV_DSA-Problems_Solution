class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs = 0
        right = -1
        count = Counter()
        result = 0
        for left in range(len(nums)):
            while pairs < k and right < len(nums) - 1:
                right += 1
                pairs += count[nums[right]]
                count[nums[right]] += 1
            if pairs >= k:
                result += len(nums) - right
            count[nums[left]] -= 1
            pairs -= count[nums[left]]
        return result


        