class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        current = numbers[left] + numbers[right]

        while current != target:
            if current > target:
                right -= 1
            elif current < target:
                left += 1

            current = numbers[left] + numbers[right]

        return [left + 1, right + 1]