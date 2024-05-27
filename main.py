

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]
rows = ["1", "2", "3"]
columns = ["A", "B", "C"]

# Set the starting player
current_player = 'X'

# function to display the board
def display_board(board, columns, rows):
    print(f"  {columns[0]} {columns[1]} {columns[2]}")
    for i in range(3):
        # print(rows[i])
        print(rows[i] + ' ' + '|'.join(board[i]))
        print('  ' + '-' * 5)

# function to handle the players move
def get_player_move(player):
    while True:
        try:
            move = input(f"Player {player} enter your move (row and column): ")
            row, column = int(move[0]), int(move[1])
            if board[row][column] == ' ':
                board[row][column] = player
                break
            else:
                print("This cell is already taken. Please chose another one.")
        except (ValueError, IndexError):
            print("Invalid input please chose 0, 1, or 2 for the row and column numbers")

#function to check for a win
def check_win(player):
    # check the rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # check the columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # check for diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# function to check for a draw
def check_draw():
    return all(i != ' ' for row in board for i in row)

# function to switch player
def switch_player(player):
    return "0" if player == "X" else "X"


# main game loop
while True:
    ans = input("Press any key to continue, or q to quit: ")

    if ans.lower() == "q":
        break

    # display board
    display_board(board, columns, rows)

    # prompt player to move
    get_player_move(current_player)

    # check if player has won
    if check_win(current_player):
        print(f"Player {current_player} wins!")
        display_board(board, columns, rows)
        break

     # check if draw
    if check_draw():
        print("It's a draw!")
        display_board(board, columns, rows)
        break
    
    # switch player
    current_player = switch_player(current_player)
  



