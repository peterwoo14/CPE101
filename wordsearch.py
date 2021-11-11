"""
CPE 101
Section 6
Project 2
Pete Woo
pswoo@calpoly.edu

"""
def reverse_string(string: str):
    """This function reverses a string.
    Args:
        string(str): The string to be reversed
    Returns:
        str: The reversed string
    """
    return string[::-1]

def transpose_string(string: str, row_len: int):
    """This function transposes a string to make rows to columns
    Args:
        string(str): The string representing a 2D structure
        row_len(int): The number of characters in a row
    Returns:
        str: The string representating the transposed string
    """
    new_str = ""
    for column in range(0, row_len):
        for row in range(column, len(string), row_len):
            new_str += string[row]
    return new_str

def find_word(puzzle: str, word: str, row_len: int):
    """This function searches the puzzle for the given word.
    Args:
        puzzle(str): The letters of the crossword puzzle
        word(str): The word to be looked for
        row_len(int): Length of each row of the puzzle
    Returns: The row and colunn of the word searched for
    """
    reverse = reverse_string(puzzle)
    downward = transpose_string(puzzle, row_len)
    upward = transpose_string(reverse, row_len)

    search_found = "{}: ({}) row: {} column: {}"
    search_lost = "{}: word not found"
    x = puzzle.find(word)
    x = no_good(x, row_len)
    if x >= 0:
        row = x // row_len
        column = x % row_len
        result = search_found.format(word, "FORWARD", row, column)
        return result

    x = reverse.find(word)
    x = no_good(x, row_len)
    if x >= 0:
        row = (((row_len ** 2) - 1) - x) // row_len
        column = (((row_len ** 2) - 1) - x) % row_len
        result = search_found.format(word, "BACKWARD", row, column)
        return result

    x = downward.find(word)
    if x >= 0:
        row = x % row_len
        column = x // row_len
        result = search_found.format(word, "DOWN", row, column)
        return result

    x = upward.find(word)
    if x >= 0:
        row = (((row_len ** 2) - 1) - x) % row_len
        column = (((row_len ** 2) - 1) - x) // row_len
        result = search_found.format(word, "UP", row, column)
        return result
    result = search_lost.format(word)
    return result


def no_good(index: int, row_len: int):
    """This function assures valid index for searches
    Args:
        index(int): Index of the start of the word found from find
        row_len(int): Number of characters per row

    Return:
        int: Same input index if valid and -1 if invalid
    """
    i = 1
    while i <= row_len:
        no_good = (row_len * i) - 1
        if index == no_good:
            return -1
        i += 1
    return index


def display(puzzle: str, row_len: int):
    """This function displays 10x10 grid of characters.
    Args:
        puzzle(str): A string of 100 characters
        row_len(int): Number of rows in puzzle
    Return:
        str: Puzzle display
    """
    string = ""
    count = 0
    start = 0
    end = row_len
    while count < row_len:
        string = string + puzzle[start:end]
        string = string + "\n"
        start += row_len
        end += row_len
        count += 1
    return string

def main():
    """This function is the main function that will display the puzzle and location of found words.
    """
    puzzle = input()
    puzzle = puzzle.strip()
    row_len = int((len(puzzle)) ** 0.5)
    print(display(puzzle, row_len))
    words = input()
    words = words.strip()
    size = int(len(words))
    last_index = size -1
    i = 0
    while i < size:
        end = words.find(" ")
        if end == -1:
            end = len(words)
        word = words[:end]
        output = find_word(puzzle, word, row_len)
        print(output)
        i = i + (int(len(word)) + 1)
        start = int(len(word)) + 1
        words = words[start:]



if __name__ == "__main__":
    main()
