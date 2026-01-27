class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        if len(b) > len(a):
            return False
        
        freq = {} 
        
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        for num in b:
            if freq.get(num, 0) == 0:
                return False
            freq[num] -= 1
            
        return True 
