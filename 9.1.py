def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


# Create empty board
board = [[" " for _ in range(3)] for _ in range(3)]

# First player
player = "X"

# Maximum 9 turns
for turn in range(9):

    print_board(board)

    print(f"Player {player}'s turn.")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    # Check if position is empty
    if board[row][col] == " ":

        board[row][col] = player

        # Check winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print("Invalid move. Try again.")

else:
    print("Final board:")
    print_board(board)
    print("It's a draw!")