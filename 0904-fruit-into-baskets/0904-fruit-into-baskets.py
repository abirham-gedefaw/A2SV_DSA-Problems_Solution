# The first code is the brute force approch where the time complexity is o(n**2).
""""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        max_fruits = 0
        for i in range(len(fruits)):
            st = set()
            for j in range(i, len(fruits)):
                st.add(fruits[j])
                if len(st) <= 2:
                    max_fruits = max(max_fruits, j - i + 1)
                else:
                    break
        return max_fruits
"""   
# here is the optimal approch with time complexity of o(n).          
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map = {}
        max_fruits = 0
        left = 0

        for right, fruit in enumerate (fruits):
            hash_map[fruit] = hash_map.get(fruit, 0) + 1
            while len(hash_map) > 2:
                hash_map[fruits[left]] -= 1
                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
