from board import create_board
from game import play_game


def main():
    """Main entry point of the game."""
    board = create_board()
    play_game(board)


if __name__ == "__main__":
    main()
