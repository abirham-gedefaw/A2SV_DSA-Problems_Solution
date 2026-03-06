class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        right = 0
        while right < len(chars):
            n = right
            char = chars[right]
            while n < len(chars) and chars[n] == char:
                    n += 1
            count = n - right
            chars[left] = char
            left += 1

            if count > 1:
                for digit in str(count):
                    chars[left] = digit
                    left += 1
            right = n
        return left


            

        