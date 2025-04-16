# Function to display the current state of the board
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if the current player has won
def check_win(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Function to check for a draw
def is_draw(board):
    return all(space in ["X", "O"] for space in board)

# Main game function
def play_game():
    board = ["1","2","3","4","5","6","7","8","9"]  # initial board
    current_player = "X"  # X starts first
    game_on = True

    while game_on:
        display_board(board)
        move = input(f"Player {current_player}, choose a position (1-9): ")

        # Check if input is a valid number
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("❌ Invalid input. Please enter a number from 1 to 9.")
            continue

        idx = int(move) - 1  # convert to 0-based index

        # Check if cell is already taken
        if board[idx] in ["X", "O"]:
            print("⛔ That cell is already taken. Try another one.")
            continue

        # Make the move
        board[idx] = current_player

        # Check for win
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_on = False
        # Check for draw
        elif is_draw(board):
            display_board(board)
            print("🤝 It's a draw!")
            game_on = False
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
