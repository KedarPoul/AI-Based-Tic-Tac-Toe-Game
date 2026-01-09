def check_winner(board, player):
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columns
        (0, 4, 8),
        (2, 4, 6),  # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def is_draw(board):
    return " " not in board
