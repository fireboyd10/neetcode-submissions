class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = []

        for i in range(9):
            rows.append(set())
            cols.append(set())
            squares.append(set())

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if num in rows[r] or num in cols[c] or num in squares[box]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[box].add(num)

        return True
