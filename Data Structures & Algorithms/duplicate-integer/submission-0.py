class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #For loop going though the nums
        for i in range(len(nums)):
            #for loop going through the nums again adding one more index to itself itself again so it does not compare to itself
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False