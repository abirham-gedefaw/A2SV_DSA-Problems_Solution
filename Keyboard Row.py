class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        
        result = []
        for word in words:
            if set(word.lower()) <= set(first_row):
                result.append(word)
            elif set(word.lower()) <= set(second_row):
                result.append(word)
            elif set(word.lower()) <= set(third_row):
                result.append(word)
        return result
