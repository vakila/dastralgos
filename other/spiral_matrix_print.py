
def log_my_name(function):
    def new_fn(*args, **kwargs):
        #print(function.__name__)
        return function(*args, **kwargs)
    return new_fn

@log_my_name
def print_right(row, col, edges):
    start_col = col
    end_col = edges['right']
    for c in range(start_col, end_col + 1):
        print(matrix[row][c])
    new_row = row + 1
    edges['top'] = new_row
    return (new_row, end_col)

@log_my_name
def print_down(row, col, edges):
    start_row = row
    end_row = edges['bottom']
    for r in range(start_row, end_row + 1):
        print(matrix[r][col])
    new_col = col - 1
    edges['right'] = new_col
    return (end_row, new_col)

@log_my_name
def print_left(row, col, edges):
    start_col = col
    end_col = edges['left']
    for c in range(start_col, end_col - 1, -1):
        print(matrix[row][c])
    new_row = row - 1
    edges['bottom'] = new_row
    return (new_row, end_col)


@log_my_name
def print_up(row, col, edges):
    start_row = row
    end_row = edges['top']
    for r in range(start_row, end_row - 1, -1):
        print(matrix[r][col])
    new_col = col + 1
    edges['left'] = new_col
    return (end_row, new_col)


print_in_direction = {"right": print_right, "down": print_down,
            "left": print_left, "up": print_up}

next_compass = {"right": "down", "down": "left",
                "left": "up", "up": "right"}


def spiral_print(matrix):
    n = len(matrix)
    m = len(matrix[0])

    compass = "right"

    edges = {'top': 0, 'right': m-1, 'bottom': n-1, 'left': 0}

    row = 0
    col = 0

    done = False

    while not done:

        row, col = print_in_direction[compass](row, col, edges)

        if edges['bottom'] < edges['top'] or edges['right'] < edges['left']:
            done = True
        else:
            compass = next_compass[compass]


if __name__ == "__main__":

    numbers = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]

    numbers_short = numbers[:2]

    numbers_skinny = [numbers[x][:2] for x in range(len(numbers))]

    letters = [['a', 'b', 'c', 'd'],
               ['e', 'f', 'g', 'h'],
               ['i', 'j', 'k', 'l'],
               ['m', 'n', 'o', 'p']]

    for matrix in [numbers, numbers_short, numbers_skinny, letters]:
        print("Printing matrix:")
        for r in range(len(matrix)):
            print(matrix[r])
        spiral_print(matrix)
