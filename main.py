import game_art

# Initialize the game board
board = [[' ' for _ in range(3)] for _ in range(3)]
column_num = ["1", "2", "3"]

# dictionaries for translating player moves to board cordinates
rows = {"1" : 0,
        "2" : 1,
        "3" : 2
        }
columns = {"A" : 0,
           "B" : 1,
           "C" : 2
           }

# Set the starting player
current_player = 'X'

# function to display the board
def display_board(board, column_num):
    print(f"  A B C")
    for i in range(3):
        # print(rows[i])
        print(column_num[i] + ' ' + '|'.join(board[i]))
        print('  ' + '-' * 5)

# function to handle the players move
def get_player_move(player, rows, columns):
    while True:
        try:
            move = input(f"Player {player} enter your move (e.g. A1): ")
            # translate player input to board coordinates
            x = move[0].upper()
            y = move[1]
            row_num = rows[y]
            col_num = columns[x]
            # print(f"x is now {row_num}")
            # print(f"y is now {col_num}")
            row, column = row_num, col_num
            if board[row][column] == ' ':
                board[row][column] = player
                # display_board(board, column_num)
                break
            else:
                print("This cell is already taken. Please chose another one.")
        except (ValueError, IndexError, KeyError):
            print("Invalid input please chose a letter for the column and number for the row(e.g. A1 - C3)")

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

# welcome art
print(game_art.welcome_art)

# main game loop
while True:
    # display board
    display_board(board, column_num)

    # prompt player to move
    get_player_move(current_player, rows, columns)

    # check if player has won
    if check_win(current_player):
        if current_player == "X":
            display_board(board, column_num)
            print(game_art.player_X_wins_art)
            break
        else:
            display_board(board, column_num)
            print(game_art.player_O_wins_art)
            break

     # check if draw
    if check_draw():
        display_board(board, column_num)
        print(game_art.draw_art)
        break
    
    # switch player
    current_player = switch_player(current_player)
  



