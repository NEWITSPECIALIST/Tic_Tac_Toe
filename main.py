# Tic Tac Toe - 2 гравці, текстова версія
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонталі
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикалі
        [0, 4, 8], [2, 4, 6]              # діагоналі
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_draw(board):
    return all(space in ["X", "O"] for space in board)

def play_game():
    board = ["1","2","3","4","5","6","7","8","9"]
    current_player = "X"
    game_on = True

    while game_on:
        display_board(board)
        move = input(f"Гравець {current_player}, обери позицію (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("❌ Недопустимий ввід. Введи число від 1 до 9.")
            continue

        idx = int(move) - 1
        if board[idx] in ["X", "O"]:
            print("⛔ Клітинка зайнята! Спробуй іншу.")
            continue

        board[idx] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Гравець {current_player} переміг!")
            game_on = False
        elif is_draw(board):
            display_board(board)
            print("🤝 Нічия!")
            game_on = False
        else:
            current_player = "O" if current_player == "X" else "X"

# Запуск гри
play_game()
