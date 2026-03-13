class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        left = 0
        counts = Counter()
        maxi = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            maxi = max(maxi, counts[s[right]])
            if (right - left+1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            res = max(res, right - left + 1)
            
        return res

        

        