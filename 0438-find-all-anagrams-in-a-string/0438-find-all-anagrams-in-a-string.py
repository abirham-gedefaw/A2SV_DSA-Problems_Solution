class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        result = []
        if m < n:
            return result
        counter_p = Counter(p)
        counter_s = Counter(s[: n - 1])

        for i in range(n-1, m):
            counter_s[s[i]] += 1
            if counter_p == counter_s:
                result.append(i - n + 1)
            left_char = s[i - n + 1]
            counter_s[left_char] -= 1
            if counter_s[left_char] == 0:
                del counter_s[left_char]
        return result



            

        