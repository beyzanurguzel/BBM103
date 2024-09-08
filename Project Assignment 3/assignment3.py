import sys

score = 0


def is_game_over(board_over):
    # if there are two numbers in a row which are side by side and equal, it means the game has not finished
    for i in range(len(board_over)):
        for j in range(len(board_over[0]) - 1):
            if type(board_over[i][j]) == int and type(board_over[i][j + 1]) == int and board_over[i][j] == board_over[i][j + 1]:
                return False
    # if there are two numbers in a column which are on top of each other and equal, it means the game has not finished
    for j in range(len(board_over[0])):
        for i in range(len(board_over) - 1):
            if type(board_over[i][j]) == int and type(board_over[i + 1][j]) == int and board_over[i][j] == board_over[i + 1][j]:
                return False
    # if there is no such a situation like that, it means the game finished
    return True


def filling_the_blanks(fill_board):
    list_column_control = []
    list_row_control = []
    # first, we fill the blanks
    for i in range(len(fill_board)):
        for j in range(len(fill_board[0])):
            if fill_board[i][j] == ' ':
                value = i
                while value >= 1:
                    fill_board[value][j] = fill_board[value - 1][j]
                    fill_board[value - 1][j] = ' '
                    value = value - 1
    # then, we delete the rows which are empty
    for i in range(len(fill_board) - 1):
        for j in range(len(fill_board[0])):
            if fill_board[i][j] == ' ':
                list_row_control.append('empty')
        if len(list_row_control) == len(fill_board[0]):
            fill_board.pop(i)
        list_row_control = []
    # after that, we delete rows which are empty
    for j in range(len(fill_board[0]) - 1):
        for i in range(len(fill_board)):
            if fill_board[i][j] == ' ':
                list_column_control.append('empty')
        if len(list_column_control) == len(fill_board):
            for m in range(len(fill_board)):
                fill_board[m].pop(j)
        list_column_control = []
    # after finishing the process we print the board and the score to the screen
    print("\n")
    for rows in fill_board:
        str_board = ' '.join(map(str, rows))
        print(str_board)
    print("\n")
    print("Your score is:{}\n".format(score))
    # we check if game is over
    if is_game_over(fill_board):
        print("Game over")
    else:
        play_game(fill_board)


def deleting_numbers(delete_board, row3, column, value):
    global score
    # if the neighbours are equal to our value, we convert them to ' '
    if 0 <= row3 < len(delete_board) and 0 <= column < len(delete_board[0]) and delete_board[row3][column] == value:
        delete_board[row3][column] = ' '
        # we update the score by adding every value we delete
        score += value
        # we check if the neighbours are equal to the value; if they are, we also check their neighbours by calling the function again
        if 0 <= column + 1 < len(delete_board[0]):
            deleting_numbers(delete_board, row3, column + 1, value)
        if 0 <= column - 1 < len(delete_board[0]):
            deleting_numbers(delete_board, row3, column - 1, value)
        if 0 <= row3 + 1 < len(delete_board):
            deleting_numbers(delete_board, row3 + 1, column, value)
        if 0 <= row3 - 1 < len(delete_board):
            deleting_numbers(delete_board, row3 - 1, column, value)


def play_game(board):
    row1, column1 = input("Please enter a row and a column number:").split()
    # we convert our row1 and column1 to index number
    row1 = int(row1) - 1
    column1 = int(column1) - 1
    # we check if the input is appropriate or not
    if row1 >= len(board) or row1 < 0:
        print("Please enter a correct size!")
        play_game(board)
    if column1 >= len(board[row1]) or column1 < 0:
        print("Please enter a correct size!")
        play_game(board)
    value = board[row1][column1]
    # if nothing is wrong, we call our delete function to remove neighbours of the value
    deleting_numbers(board, row1, column1, value)
    # after removing neighbour, we fill the blanks by calling our fill function
    filling_the_blanks(board)


with open(sys.argv[1], "r") as input_file:
    # we convert our txt to a list of lists
    lines = input_file.read().splitlines()
    game_board = []
    for row in lines:
        game_board.append([int(value) for value in row.split()])
    # we print the game_board to the screen for player
    for row in game_board:
        row_str = ' '.join(map(str, row))
        print(row_str)
    print("\n")
    print("Your score is:{} \n".format(0))
    play_game(game_board)
