from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # Count X's and O's using all()
        x_count = sum(sum(1 for c in row if c == 'X') for row in board)
        o_count = sum(sum(1 for c in row if c == 'O') for row in board)

        if o_count > x_count or x_count - o_count > 1:
            return False

        def win(player: str) -> bool:
            # Rows
            if any(all(c == player for c in row) for row in board):
                return True
            # Columns
            if any(all(board[r][c] == player for r in range(3)) for c in range(3)):
                return True
            # Diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        x_win = win('X')
        o_win = win('O')

        if x_win and o_win:
            return False
        if x_win and x_count != o_count + 1:
            return False
        if o_win and x_count != o_count:
            return False

        return True
