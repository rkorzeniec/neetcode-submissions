class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                if val in rows[row] or val in cols[col]:
                    return False

                box_row = (row // 3)
                box_col = (col // 3)
                if val in boxes[(box_row, box_col)]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[(box_row, box_col)].add(val)

        return True
            