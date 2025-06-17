def generate_board():
    """Return a 12x12 grid with factor labels."""
    board = []
    for row in range(1, 13):
        row_data = []
        for col in range(1, 13):
            if row >= col:
                row_data.append(f"{row}×{col}")
            else:
                row_data.append(f"{col}×{row}")
        board.append(row_data)
    return board

def display_board(board):
    """Print the board with row and column labels."""
    header = " " * 5 + " ".join(f"{c:>7}" for c in range(1, 13))
    print(header)
    for idx, row in enumerate(board, start=1):
        print(f"{idx:>3} " + " ".join(f"{cell:>7}" for cell in row))

if __name__ == "__main__":
    board = generate_board()
    display_board(board)
