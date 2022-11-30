"""
Four-in-a-Row
Chip line up game
"""

import sys

# const to display the playing field
EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

# note, if BOARD_WIDTH changes, then update BOARD_TEMPLATE and COLUMN_LABELS
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# template string for the field
BOARD_TEMPLATE = """
    
     1234567
    +-------+
    |{}{}{}{}{}{}|
    |{}{}{}{}{}{}|
    |{}{}{}{}{}{}|
    |{}{}{}{}{}{}|
    |{}{}{}{}{}{}|
    |{}{}{}{}{}{}| 
    +-------+"""

def main():
    """Performs one game 'Four in a row'"""

    print("""Four-in-a-Row
    
    Two players take turns dropping chips into one of the seven columns.
    It is necessary that the chips are in a row either vertically or horizontally or diagonally.
    """
          )
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:  # stroke processing
        # output playing field
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # check for a win or a draw
        if is_winner(player_turn, game_board):
            display_board(game_board)  # last one view playing field
            print("Player {} has won!".format(player_turn))
            sys.exit()

        elif is_full(game_board):
            display_board(game_board)  # last one view playing field
            print("There is a tie!")
            sys.exit()

        # the move is passed to another player
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X

def get_new_board():
    """
    keys column_index, row_index is int and values it is one string with "X", "O" or "." (space).
    :return: dict which is playing field
    """
    board = {}
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board

def display_board(board):
    """
    Prepare list, transmitted sting methods format() for template playing field.
    List contains all chips and blanks.

    :param board:
    :return: output window with chips and field
    """
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])
    # output field
    print(BOARD_TEMPLATE.format(*tile_chars))

def get_player_move(player_tile, board):
    """
    Prompts you to select a column
    :param player_tile:
    :param board:
    :return: tuple
    """
    while True:  # will not enter a valid move
        print(f"Player {player_tile}, enter 1 to {BOARD_WIDTH} or QUIT:")

        response = input("> ").upper().strip()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter a number from 1 to {BOARD_WIDTH}")
            continue

        column_index = int(response) - 1  # -1, because index start with 0

        # If column full, ask the move again
        if board[(column_index, 0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue  # ask the move again

        # Start bottom, find first empty cell
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)

def is_full(board):
    """
    True - "board" are no empty seats left
    False - "board" are empty seats left
    :param board:
    :return: bool
    """
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):

            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False

    return True  # the cell is full

def is_winner(player_tile, board):
    """
    True - "player_tile" in 4 rows otherwise False
    :param player_tile:
    :param board:
    :return: bool
    """
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # four to the right will check
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index)]
            tile_3 = board[(column_index + 2, row_index)]
            tile_4 = board[(column_index + 3, row_index)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # four to the down will check
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index, row_index + 1)]
            tile_3 = board[(column_index, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # four to the diagonal down to the left will check
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index + 1)]
            tile_3 = board[(column_index + 2, row_index + 2)]
            tile_4 = board[(column_index + 3, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

            # four to the diagonal down to the right will check
            tile_1 = board[(column_index + 3, row_index)]
            tile_2 = board[(column_index + 2, row_index + 1)]
            tile_3 = board[(column_index + 1, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
    return False

if __name__ == "__main__":
    main()