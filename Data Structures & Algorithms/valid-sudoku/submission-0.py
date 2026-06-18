class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)] 
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                d=board[r][c]
                d_idx=(r//3)*3+(c//3)
                if(d in rows[r] or d in cols[c] or d in box[d_idx]):
                    return False
                rows[r].add(d)
                cols[c].add(d)
                box[d_idx].add(d)
        return True

        