class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        palendrome = True

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                palendrome = False
                break
            left += 1
            right -= 1
        return palendrome
        