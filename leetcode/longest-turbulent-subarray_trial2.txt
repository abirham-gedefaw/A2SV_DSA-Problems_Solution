class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        max_len = 1
        curr_len = 1

        prev_trend = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if prev_trend == -1:
                    curr_len += 1
                else:
                    curr_len = 2
                prev_trend = 1
            elif arr[i] < arr[i-1]:
                if prev_trend == 1:
                    curr_len += 1
                else:
                    curr_len = 2
                prev_trend = -1
            else:
                curr_len = 1
                prev_trend = 0
            max_len = max(max_len, curr_len)
        return max_len