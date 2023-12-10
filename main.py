
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if all(cell == player for cell in board[i:i+3]) or all(cell == player for cell in board[i::3]):
            return True
    if all(cell == player for cell in board[0::4]) or all(cell == player for cell in board[2:7:2]):
        return True
    return False


def is_board_full(board):
    return all(cell != '' for cell in board)

def tic_tac_toe():
    board = ['', '', '',
             '', '', '',
             '', '', '']

    current_player = 'X'

    while True:
        print_board(board)

        # Get the user's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == '':
                board[move] = current_player
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check for a win
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
