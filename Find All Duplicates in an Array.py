class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        result = []
        for key, value in hash_map.items():
            if value == 2:
                result.append(key)

        return result
