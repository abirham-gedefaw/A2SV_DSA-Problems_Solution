class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set("aeiou")
        count = 0
        for i in range(len(word)):
            found_vowels = set()
            for char in word[i:]:
                if char not in vowels:
                    break
                found_vowels.add(char)
                if len(found_vowels)== 5:
                    count += 1
        return count
                
            
