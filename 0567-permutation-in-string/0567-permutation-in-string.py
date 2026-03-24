class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:m])

        if count_s2 == count_s1:
            return True

        left = 0
        for right in range(m, n):
           count_s2[s2[right]] += 1
           count_s2[s2[left]] -= 1
           if count_s2[s2[left]] == 0:
            del count_s2[s2[left]]
           left += 1
           if count_s2 == count_s1:
            return True
        return False

        