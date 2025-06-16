import random

def generate_bingo_board():
    board = []
    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }
    for letter in 'BINGO':
        numbers = random.sample(ranges[letter], 5)
        board.append(numbers)
    # Set the center space to "FREE"
    board[2][2] = 'FREE'
    return board

def display_board(board):
    headers = ' '.join(f"{c:^5}" for c in 'BINGO')
    print(headers)
    for row in zip(*board):
        print(' '.join(f"{str(cell):^5}" for cell in row))

if __name__ == "__main__":
    board = generate_bingo_board()
    display_board(board)
