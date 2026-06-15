import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window_heap = [(nums[i], i) for i in range(k-1)]
        heapq.heapify_max(window_heap)

        l = 0
        r = k - 1
        while r < len(nums):
            heapq.heappush_max(window_heap, (nums[r], r))
            result.append(window_heap[0][0])
            
            l += 1
            while window_heap and window_heap[0][1] < l:
                heapq.heappop_max(window_heap)

            r += 1

        return result