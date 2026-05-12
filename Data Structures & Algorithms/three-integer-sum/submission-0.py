class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Step 1: sort to enable two pointers from the 2 sum question
        result = []

        # Step 2: fix the first element (i) you only need up to -2 dont need to iterate through everything
        for i in range(len(nums) - 2):
            
            # Skip duplicate values for i (prevents duplicate triplets)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # Step 3: two-pointer search
            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if current < 0:
                    left += 1

                elif current > 0:
                    right -= 1

                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Step 4: skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Step 5: skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result