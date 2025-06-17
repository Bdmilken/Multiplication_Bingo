def generate_board():
    """Return a 12x12 grid of blank strings."""
    return [["" for _ in range(12)] for _ in range(12)]

def display_board(board):
    """Print the board with row and column labels."""
    header = "    " + " " .join(f"{c:>4}" for c in range(1, 13))
    print(header)
    blank_cell = " " * 4
    for idx in range(1, 13):
        print(f"{idx:>3} " + " ".join(blank_cell for _ in range(12)))

if __name__ == "__main__":
    board = generate_board()
    display_board(board)
