import sys


def find_empty_spaces(sudoku, output_file, step):
    # we try to find an empty cell
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                row, column = i, j
                # if we find an empty cell then we try to put a value on it
                control = finding_value(sudoku, row, column)
                # if we find a value which is the only solution for the empty cell , we write this step to the output file.
                if control[0]:
                    step += 1
                    output_file.write('-' * 18)
                    output_file.write("\n")
                    output_file.write('Step {} - {} @ R{}C{}'.format(step, control[1], row + 1, column + 1))
                    output_file.write("\n")
                    output_file.write('-' * 18)
                    output_file.write("\n")
                    # after the information about the step, we convert our sudoku array to a matrix and write it to the output file.
                    for row in sudoku:
                        row_str = ' '.join(map(str, row))
                        output_file.write(row_str)
                        output_file.write("\n")
                    # then we leave the loop and start a new one by calling the function again.
                    # because there might appear a cell with only one possibility before our completed cell
                    find_empty_spaces(sudoku, output_file, step)


def finding_value(sudoku, row, column):
    list1 = []
    value = 1
    while value <= 9:
        misplace = False
        # first, we test the row
        for testing in range(9):
            if sudoku[row][testing] == value:
                misplace = True
        # if there is no cell which is equal to our value in the row, we test columns
        if not misplace:
            for testing in range(9):
                if sudoku[testing][column] == value:
                    misplace = True
            # then, we test the square which the cell belongs
            if not misplace:
                new_column = column - (column % 3)
                new_row = row - (row % 3)
                for square_row in range(3):
                    for square_column in range(3):
                        if sudoku[new_row + square_row][new_column + square_column] == value:
                            misplace = True
        # if the value fits the cell we append it to our list to make sure if there are no other values which fit the cell
        if not misplace:
            list1.append(value)
        value += 1
    # if the list have more than one element, it means we cannot put a value on it
    if len(list1) == 1:
        sudoku[row][column] = list1[0]
        # for writing the value in other function we return the value
        return True, list1[0]
    else:
        return False, None


def main():
    with open(sys.argv[1], "r") as input_file:
        # we convert our matrix to a list which contains the rows of the sudoku as elements of the list
        lines = input_file.read().splitlines()
        sudoku_board = []
        for row in lines:
            sudoku_board.append([int(value) for value in row.split()])

    with open(sys.argv[2], "w") as output_file:
        find_empty_spaces(sudoku_board, output_file, 0)
        # we write 18 times '-' character at the end of the output file to show that steps are finished
        output_file.write('-' * 18)


if __name__ == '__main__':
    main()
