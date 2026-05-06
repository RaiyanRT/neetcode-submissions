class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer1 = 0
        answer2 = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer1 = i
                    answer2 = j
        return [answer1, answer2]
        