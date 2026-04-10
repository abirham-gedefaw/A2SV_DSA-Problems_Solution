class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        hash_map = {')': '(', '}':'{', ']' : '['}

        for char in s:
            if char in hash_map:
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
        