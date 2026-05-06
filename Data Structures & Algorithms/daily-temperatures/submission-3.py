class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        # output = [0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             output[i] = j-i
        #             break

        # return output


        answer = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stk_t, stk_i = stack.pop()
                answer[stk_i] = i - stk_i

            stack.append((t,i))

        return answer



