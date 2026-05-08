class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # areas = []
        # for index in range(len(heights)):
        #     counter = 1  # include the bar itself
        #     h = heights[index]

        #     # expand left
        #     left = index - 1
        #     while left >= 0 and heights[left] >= h:
        #         counter += 1
        #         left -= 1

        #     # expand right
        #     right = index + 1
        #     while right < len(heights) and heights[right] >= h:
        #         counter += 1
        #         right += 1

        #     areas.append(counter * h)

        # return max(areas)

        stack = []
        areas = []


        for index, value in enumerate(heights):
            if not stack:
                stack.append((index,value))
            elif heights[index] >= stack[-1][1]:
                stack.append((index,value))
            else:
                start_index = index
                while stack and stack[-1][1] > value:
                    popped = stack.pop()
                    areas.append(popped[1] * (index - popped[0]))
                    start_index = popped[0]
                stack.append((start_index, value))
        
        while stack:
            popped = stack.pop()
            areas.append(popped[1] * (len(heights) - popped[0]))





        return max(areas)

