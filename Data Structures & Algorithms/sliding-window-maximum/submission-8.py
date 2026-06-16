import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque() # queue of indexes

        l = 0
        r = 0
        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)
            if l > queue[0]:
                queue.popleft()

            if (r+1) >= k:
                result.append(nums[queue[0]])
                l += 1

            r += 1

        return result