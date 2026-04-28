class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left +(right - left) // 2
            k_rows = mid * (mid + 1) // 2
            if k_rows == n:
                return mid
            elif k_rows > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
        