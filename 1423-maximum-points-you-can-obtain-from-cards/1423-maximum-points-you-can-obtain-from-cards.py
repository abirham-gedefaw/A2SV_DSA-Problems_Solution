class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        min_subarraySum = float('inf')
        left = curr = 0
        for right, val in enumerate(cardPoints):
            curr += val
            if right - left + 1 > size:
                curr -= cardPoints[left]
                left += 1
            if right - left + 1 == size:
                min_subarraySum = min(min_subarraySum, curr)
        return sum(cardPoints) - min_subarraySum
        