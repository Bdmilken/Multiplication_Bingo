def generate_board():
    """Return a 12x12 grid with sequential numbers 1..144."""
    board = []
    num = 1
    for _ in range(12):
        row = list(range(num, num + 12))
        board.append(row)
        num += 12
    return board

def display_board(board):
    """Print the board with row and column labels."""
    header = "    " + " " .join(f"{c:>4}" for c in range(1, 13))
    print(header)
    for idx, row in enumerate(board, start=1):
        print(f"{idx:>3} " + " ".join(f"{cell:>4}" for cell in row))

if __name__ == "__main__":
    board = generate_board()
    display_board(board)
