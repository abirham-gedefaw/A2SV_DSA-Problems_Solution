class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        adjacent_pair = 0
        max_window_size = 0
        left = 0
        for right in range(1, len(s)):
            adjacent_pair += s[right] == s[right - 1]
            while adjacent_pair > 1:
                adjacent_pair -= s[right] == s[right - 1]
                left += 1
            max_window_size = max(max_window_size, right - left + 1)
        return max_window_size
        