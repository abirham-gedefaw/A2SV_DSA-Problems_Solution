class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = []
        number = abs(num)
        
        if num == 0:
            return 0

        while number != 0:
            digit = number % 10
            digits.append(digit)
            number //= 10

        digits.sort()
        
        if num < 0:
            digits = digits[::-1]
        else:
            if  len(digits) > 0 and digits[0] == 0 :
                for i in range(len(digits)):
                    if digits[i] > 0:
                        digits[0], digits[i] = digits[i], digits[0]
                        break

        ans = int("".join(map(str, digits)))
        return (-ans if num < 0 else ans)