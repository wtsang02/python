from ticktactoematrix import TickTacToeMatrix


def create_tick_tack_toe_board(w, h):
    return TickTacToeMatrix(w, h)


def print_instructions():
    print("X player goes first. type in x,y as the input of where you want to put the X or O. ")
    print("Example, if I want to put my symbol at the middle, I would type 1,1 ")


def main():
    print_instructions()
    board = create_tick_tack_toe_board(3, 3)
    user_input = None
    while not board.is_complete():
        while user_input is None or board.has_played_symbol(width, height):
            board.start_turn()
            user_input = input()
            array_input = user_input.split(',')
            width = int(array_input[0])
            height = int(array_input[1])
        board.set_symbol_at(width, height)
    board.complete_game()


if __name__ == "__main__":
    main()
