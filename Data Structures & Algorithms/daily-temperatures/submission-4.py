class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        # output = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             output[i] = j-i
        #             break

        # return output


        # Initialize answer list with 0s
        # Default is 0 because if no warmer day exists, we leave it as 0
        answer = [0] * len(temperatures)

        # Stack will store pairs: (temperature, index)
        # meaning temperatures in the stack go from high -> low
        stack = []

        # Loop through each day
        for i, t in enumerate(temperatures):

            # This while loop tries to resolve previous days
            # as soon as we find a warmer temperature
            while stack and stack[-1][0] < t:
                stk_t, stk_i = stack.pop()

                # Calculate how many days it took
                answer[stk_i] = i - stk_i

                # Keep looping because current temp might resolve
                # multiple previous colder days

            # Keep appending so long as the while loop is resolved
            stack.append((t, i))

        return answer



