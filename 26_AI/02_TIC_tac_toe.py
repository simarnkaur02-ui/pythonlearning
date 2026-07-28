#write code for tic tac toe
# 1. Create a 3x3 board
# 2. Take input from player 1 and player 2 
# 3. Check if the  input is valid 
# 4.Check if the game is over
# 5. Check if the game is a draw 
# 6. Check if the game is won
# 7. Print the board after each move 
# 8. print the winner
# 9. Print the draw message
# 10. Print the invalid input message
# 11. Print the game over message

def greet():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X") 
    print("Player 2 is O")
    print("let's start the game!")
    
          
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n  1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " | ".join(row))
        if i < 3:
            print("  " + "-" * 9)
    print()

def is_valid_move(board, r, c):
    return 0 <= r < 3 and 0 <= c < 3 and board[r][c] == " "

def check_winner(board, player):
    # rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # columns
    for c in range(3):
        if all(board[r][c] == player for r in range(3)):
            return True
    # diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            s = input(f"Player {player} enter row and column (e.g. 1 3): ").strip().split()
            if len(s) != 2:
                print("Invalid input. Enter two numbers.")
                continue
            r, c = int(s[0]) - 1, int(s[1]) - 1
            return r, c
        except ValueError:
            print("Invalid input. Use numbers 1-3.")

def main():
    board = create_board()
    current = "X"
    print("Tic Tac Toe - Player X goes first.")
    print_board(board)

    while True:
        r, c = get_move(current)
        if not is_valid_move(board, r, c):
            print("Invalid move. Try again.")
            continue
        board[r][c] = current
        print_board(board)

        if check_winner(board, current):
            print(f"Player {current} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        current = "O" if current == "X" else "X"

    print("Game over.")

    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye.")
