class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # first find the shortest string in strs.
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        # compiare each charactors of a string in strs.
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i] 
            i += 1
        return s[:i]   
