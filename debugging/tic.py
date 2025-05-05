#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check horizontal and vertical lines
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal lines
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        valid_input = False
        
        while not valid_input:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                
                # Validate the input
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Row and column must be between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    board[row][col] = player
                    valid_input = True
            except ValueError:
                print("Invalid input! Please enter integers only.")
        
        # Switch players
        player = "O" if player == "X" else "X"

    print_board(board)
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
