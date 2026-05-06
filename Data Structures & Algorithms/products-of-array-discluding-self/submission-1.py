class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        resultList = []

        

        # Old solution with O(n) squared
        # for index, value in enumerate(nums):
        #     answer = 1
        #     for index2, value2 in enumerate(nums):
        #         if index != index2:
        #             answer = answer * value2
        #     resultList.append(answer)
                    
        zero_count = 0
        zero_pos = 0
        answer = 1

        for index, value in enumerate(nums):
            if value == 0:
                zero_count += 1
                zero_pos = index

        if zero_count == 0:
        
            #Solution that works with the division operator
            for value in nums:
                answer = answer * value

            resultList = [answer] * len(nums)

            for index in range(len(nums)):
                if nums[index] == 0:
                    resultList[index] = 0
                else:
                    resultList[index] = int(resultList[index]/nums[index])
            



        elif zero_count == 1:
            for value in nums:
                if value != 0:
                    answer = answer * value
            resultList = [0] * len(nums)
            resultList[zero_pos] = answer

        else:
            resultList = [0] * len(nums)



        return resultList