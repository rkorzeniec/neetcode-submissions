class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, len(matrix[0]))

            val = matrix[row][col]
            if val == target:
                return True
            elif val <= target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False