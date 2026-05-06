class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        
        for num in nums:

            # if we havent seen this number before, add it to the dictionary with a count of 0

            if num not in count:
                count[num] = 0

            # increment the count of this number by 1

            count[num] += 1

        # create n+1 empty buckets (index represents frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # drop each number into its frequency bucket
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        
        for bucket in buckets[::-1]:
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result
