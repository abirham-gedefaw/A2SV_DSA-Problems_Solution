class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1
        