class Solution:
    def maxArea(self, heights: List[int]) -> int:

        biggest = 0

        left = 0
        right =  len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                current = heights[left] * (right - left)
                left += 1
            else:
                current = heights[right] * (right - left)
                right -=1
            if current > biggest:
                biggest = current
            

        return int(biggest)
        