class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        even_position = (n + 1) // 2
        odd_position = n // 2

        return (pow(5, even_position, mod) * pow(4, odd_position, mod)) % mod 

        