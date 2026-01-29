class Solution(object):
    def isValidSudoku(self, board):
        filled = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    row = (r, board[r][c])
                    col = (board[r][c], c)
                    box = (r // 3, c // 3, board[r][c])

                    if row in filled or col in filled or box in filled:
                        return False

                    filled.append(row)
                    filled.append(col)
                    filled.append(box)

        return True

board = eval(input())

result = Solution().isValidSudoku(board)

print(result)
