class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                # Box index: 0–8
                box_idx = (i // 3) * 3 + (j // 3)

                # Check if already seen
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_idx]):
                    return False

                # Mark as seen
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

        return True