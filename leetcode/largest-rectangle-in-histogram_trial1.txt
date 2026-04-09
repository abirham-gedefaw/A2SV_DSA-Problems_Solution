class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                poped_index = stack.pop()
                h = heights[poped_index]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                area = h * w
                ans = max(ans, area)
            stack.append(i)
        return ans

        