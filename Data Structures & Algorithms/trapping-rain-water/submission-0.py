class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        
        prefix: list[int] = []
        max_left = 0
        for i in range(l):
            max_left = max(max_left, height[i])
            prefix.append(max_left)

        suffix = [0] * l
        max_right = 0
        for i in range(l - 1, -1, -1):
            max_right = max(max_right, height[i])
            suffix[i] = max_right

        water = 0
        for i in range(l):
            current_water = min(prefix[i], suffix[i]) - height[i]
            if current_water > 0:
                water += current_water

        return water