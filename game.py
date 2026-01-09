from board import display_board
from utils import check_winner, is_draw
from minimax import best_move


def play_game(board):
    """Controls the main game loop."""

    while True:
        display_board(board)

        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"

        if check_winner(board, "O"):
            display_board(board)
            print("AI wins!")
            break
