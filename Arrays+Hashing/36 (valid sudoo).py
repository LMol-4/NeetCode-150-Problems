class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init dicionaries
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        squares = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num.isnumeric():
                    # check row
                    rows[i][num] = rows[i].get(num, 0) + 1
                    if rows[i][num] > 1:
                        return False

                    # check cols
                    columns[j][num] = columns[j].get(num, 0) + 1
                    if columns[j][num] > 1:
                        return False

                    # checksquares
                    square_no = (i // 3) * 3 + (j // 3)
                    squares[square_no][num] = squares[square_no].get(num, 0) + 1
                    if squares[square_no][num] > 1:
                        return False

        return True
