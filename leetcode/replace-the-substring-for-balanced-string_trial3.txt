class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        count = Counter(s)

        if all(count[char] == target for char in "QWER"):
            return 0
        min_len = len(s)
        left = 0
        for right in range(len(s)):
            count[s[right]] -= 1
            while left <= right and all(count[char] <= target for char in "QWER"):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
        return min_len
        