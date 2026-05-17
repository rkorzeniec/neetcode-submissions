class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        cache = set(nums)
        max_len = 0

        for i in range(len(nums)):
            if nums[i] - 1 in cache:
                continue
            
            current_num = nums[i]
            streak = 1

            while current_num + 1 in cache:
                current_num += 1
                streak += 1

            max_len = max(max_len, streak)

        return max_len