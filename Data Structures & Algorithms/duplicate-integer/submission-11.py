class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:     
        
        # A set of all seen number
        seen = set()
        
        #iterate through the list and check in the set if there is a repeated number
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False