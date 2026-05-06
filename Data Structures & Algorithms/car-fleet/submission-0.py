class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []


        # Compute the times of each car
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        cars.sort(reverse=True)

        for position, time in cars:
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)

        return len(stack)