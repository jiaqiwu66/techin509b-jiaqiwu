from typing import List

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    try:
        # Ensure all rows have the same length
        row_lengths = [len(row) for row in input_board]
        assert all(length == row_lengths[0] for length in row_lengths), "Input board rows have different lengths."
        
        # Get the number of rows and columns in the board
        row = len(input_board)
        col = len(input_board[0])

        # Create a list of lists from the input board
        board_arr = [list(line) for line in input_board]

        # Check if the starting coordinates are valid and if the cell contains the 'old' value
        if (0 <= x < row and 0 <= y < col) and board_arr[x][y] == old:
            dfs(board_arr, x, y, row, col, old, new)

        # Convert the modified board back to a list of strings
        res = ["".join(line) for line in board_arr]

        return res
    except Exception as e:
        print("An error occurred:", str(e))
        return input_board


def dfs(board_arr: List[List[str]], x: int, y: int, row: int, col: int, old: str, new: str):
    # Mark the current cell as 'new'
    board_arr[x][y] = new
    for direct in directions:
        # Check adjacent cells for flood fill
        x_ = x + direct[0]
        y_ = y + direct[1]
        if 0 <= x_ < row and 0 <= y_ < col and board_arr[x_][y_] == old:
            dfs(board_arr, x_, y_, row, col, old, new)


board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....


# New test case
board2 = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#......",
    "....###........#......",
    "....#..........#......",
    "....############......",
]

modified_board = flood_fill(input_board=board2, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output2:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ....###~~~~~~~~#......
# ....#~~~~~~~~~~#......
# ....############......