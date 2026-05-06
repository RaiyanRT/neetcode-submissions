class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        for index in range(len(heights)):
            counter = 1  # include the bar itself
            h = heights[index]

            # expand left
            left = index - 1
            while left >= 0 and heights[left] >= h:
                counter += 1
                left -= 1

            # expand right
            right = index + 1
            while right < len(heights) and heights[right] >= h:
                counter += 1
                right += 1

            areas.append(counter * h)

        return max(areas)