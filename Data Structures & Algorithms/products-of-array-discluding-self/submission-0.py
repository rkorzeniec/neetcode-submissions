class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = nums[:]
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        product = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result