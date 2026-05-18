class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result: set[list[int]] = set()

        print(nums)
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    sequence = tuple([nums[i], nums[left], nums[right]])
                    result.add(sequence)
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(result)

        