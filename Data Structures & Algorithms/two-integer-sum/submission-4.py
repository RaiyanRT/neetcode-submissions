class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store each number we've seen and its index
        # key = number, value = index
        seen = {}

        # Loop through nums while keeping track of index and number
        for i, num in enumerate(nums):

            # Find the number we need to reach the target
            complement = target - num

            # If we've already seen that number,
            # return its index and the current index
            if complement in seen:
                return [seen[complement], i]

            # Otherwise, remember the current number and its index
            seen[num] = i