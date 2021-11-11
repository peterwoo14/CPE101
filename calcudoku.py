"""
CPE 101
Section 6
Project 3
Pete Woo
pswoo@calpoly.edu

"""


def get_num_cages():
    """This function asks the user to input the number of cages.
    Return:
        int: Number of cages
    """
    i = 1
    while i > 0:
        cages = input()
        if cages.isdigit() == True:
            cages = int(cages)
            if cages > 0:
                return cages

def get_cage_info(num):
    """This function asks the user to input information about the cages.
    Args:
        num(int): The number of lists
    Return
        list: List of cage information
    """
    
    cages = []
    for i in range(num):
        info = input()
        new_info = info.split()
        info = [int(e) for e in new_info]
        cages.append(info)
    return cages

def create_grid(dim):
    """This function creates a grid of dim * dim.
    Args:
        dim(int): The dimension of the grid
    Return:
        list: A list of lists of 0s
    """
    grid = []
    row = []
    element = 0
    for i in range(dim):
        for i in range(dim):
            row.append(element)
        grid.append(row)
        row = []
    return grid

def print_grid(grid):
    """This function prints the grid.
    Args:
        grid(list): The grid of numbers that solve the puzzle
    """
    grid_size = len(grid)
    row = 0
    for i in range(grid_size):
        grid_row = grid[row]
        puzzle_row = "".join([str(element) for element in grid_row])
        print(puzzle_row)
        row += 1


def transpose_grid(grid):
    """Transposes a grid.
    Args:
        grid(list): A grid
    Return:
        list: A list of lists which is a transposed version of the grid
    """
    transposed_grid = []
    transposed_row = []
    grid_size = len(grid)
    row = 0
    column = 0
    for i in range(grid_size):
        for i in range(grid_size):
            transposed_row.append(grid[row][column])
            row += 1
        transposed_grid.append(transposed_row)
        transposed_row = []
        row = 0
        column += 1
    return transposed_grid


def validate_rows(grid):
    """This function validates that there are no repeating numbers all rows.
    Args:
        grid(list): A grid
    Return:
        bool: True if valid and False if not
    """
    grid_size = len(grid)
    count = grid_size - 1
    cell_test = grid_size -1
    testing_column = 1
    testing_row = 0
    controlled_column = 0
    controlled_row = 0
    tallies = 1
    for i in range(grid_size):
        for i in range(count):
            control = grid[controlled_row][controlled_column]
            for i in range(cell_test):
                test = grid[testing_row][testing_column]
                if test == control and test != 0 and control != 0:
                    return False
                testing_column += 1
            tallies += 1
            controlled_column += 1
            testing_column = tallies + 0
            cell_test -= 1
        testing_column = 1
        controlled_column = 0
        testing_row += 1
        controlled_row += 1
        tallies = 1
        cell_test = grid_size - 1
    return True


def validate_cols(grid):
    """This function validates that there are no repeating numbers all column.
    Args:
        grid(list): A grid
    Return:
        bool: True if valid and False if not
    """
    transposed_grid = transpose_grid(grid)
    validate = validate_rows(transposed_grid)
    return validate


def validate_single_cage(cage, grid):
    """This function validates that each cage adds up to its specified value.
    Args:
        cage(list): A list of information about a cage
        grid(list): A grid
    Return:
        bool: True if valid and False if not
    """
    sum_in_cage = 0
    full = True
    for i in range(2, len(cage)):
        row = cage[i] // 5
        column = cage[i] % 5

        if grid[row][column] == 0:
            full = False
        sum_in_cage += grid[row][column]

    if full is True:
        if sum_in_cage == cage[0]:
            return True
        else:
            return False
    else:
        if sum_in_cage >= cage[0]:
            return False
        else:
            return True


def validate_cages(grid, cages):
    """This function validates that all cages add up to their specified value.
    Args:
        grid(list): A grid
        cages(list): A list of cage information
    Return:
        bool: True if valid and False if not
    """
    for cage in cages:
        if validate_single_cage(cage, grid) == False:
            return False
    return True

def validate_all(grid, cages):
    """This function validates if rows, columns, and cages are valid.
    Args:
        grid(list): A grid
        cages(int): A list of cage information
    Return:
        bool: True if rows columns and cages are all valid
    """
    if validate_rows(grid) == True and validate_cols(grid) == True and validate_cages(grid, cages) == True:
        return True
    else:
        return False

def main():
    """This function is the main function of Calcudoku.
    """
    grid = create_grid(5)
    num = get_num_cages()
    cages = get_cage_info(num)
    index = 0

    while index < 25:
        row = index // 5
        column = index % 5
        grid[row][column] += 1
        if grid[row][column] > 5:
            grid[row][column] = 0
            index -= 1
            if index < 0:
                index = 0
        elif validate_all(grid, cages) is True:
            index += 1
    print_grid(grid)


if __name__ == "__main__":
    main()
