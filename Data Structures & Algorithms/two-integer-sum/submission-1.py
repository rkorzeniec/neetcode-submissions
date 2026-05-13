class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in cache:
                return [cache[diff], i]
            
            cache[nums[i]] = i