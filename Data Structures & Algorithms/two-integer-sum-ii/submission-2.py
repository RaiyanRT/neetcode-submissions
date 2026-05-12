class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # They are in ascending order essentailly with no edge case as there will always be an answer.
        # Compute the first sum of the left and right pointer sum. 
        # If the sum is greater than the target -1 index on the right pointer
        # if the sum is less than the target +1 on the left pointer
        left = 0
        right = len(numbers) - 1

        current = numbers[left] + numbers[right]

        while current != target:
            if current > target:
                right -= 1
            elif current < target:
                left += 1

            current = numbers[left] + numbers[right]

        return [left + 1, right + 1] # we need to give answer in 1 index but python is 0 indexed so you add one.