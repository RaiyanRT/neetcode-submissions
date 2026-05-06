class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []


        # Compute the times of each car
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        # sort cars by position will make time complexity O Log N
        cars.sort(reverse=True)

        # If stack empty append whatever time as its sorted by position from biggest to shortest. 
        # Then check their timings, and if their timings is shorter append that to the stack.
        for position, time in cars:
            if not stack:
                stack.append(time)
            if time > stack[-1]:
                stack.append(time)

        return len(stack)