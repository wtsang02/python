import numpy as np
from abc import abstractmethod


class TickTacToeMatrix:
    _matrix = None
    _turn = 0
    _rules = None
    DEFAULT_SYMBOL = ' '
    CROSS_VALUE = "X Player"
    CIRCLE_VALUE = "O Player"
    PLAYER_VALUE = {
     0: CROSS_VALUE,
     1: CIRCLE_VALUE
    }

    def __init__(self, w, h):
        self._matrix = np.matrix([[self.DEFAULT_SYMBOL for x in range(w)] for y in range(h)])
        self._rules = [
            DiagonalRule(self._matrix),
            HorizontalRule(self._matrix),
            VerticalRule(self._matrix),
            TieRule(self._matrix)
        ]

    def start_turn(self):
        print("Its now {} turn".format(self.current_player()))
        print(self)

    def set_symbol_at(self, w, h):
        if self.current_player() == self.CROSS_VALUE:
            self._set_cross_at(w, h)
        else:
            self._set_circle_at(w, h)

    def _set_cross_at(self, w, h):
        self._matrix[w, h] = self.CROSS_VALUE
        self.end_turn()

    def _set_circle_at(self, w, h):
        self._matrix[w, h] = self.CIRCLE_VALUE
        self.end_turn()

    def has_played_symbol(self, w, h):
        return self._matrix[w, h] != self.DEFAULT_SYMBOL

    def __repr__(self):
        return self._matrix.__repr__()

    def __str__(self):
        return self._matrix.__str__()

    def current_player(self):
        return self.PLAYER_VALUE[(self._turn % 2)]

    def end_turn(self):
        print("Player {} turn has now ended".format(self.current_player()))
        self._turn += 1

    def is_complete(self):
        return any(rule.is_completed() for rule in self._rules)

    def complete_game(self):
        if TieRule(self._matrix).is_completed():
            self.print_tie_game()
        else:
            self.print_complete_game()
        print(self)

    def print_complete_game(self):
        #lazy hack on turn
        self._turn -= 1
        print("Player {} has Won the game".format(self.current_player()))
        self._turn += 1

    def print_tie_game(self):
        print("Game completed with tie.")


class TicTacToeRule:
    matrix = None

    def __init__(self, a_matrix):
        self.matrix = a_matrix

    @abstractmethod
    def is_completed(self):
        return False

    def is_symbols_equal(self, a_list):
        #print("is_symbols_equal")
        first_value = a_list[0]
        if first_value != TickTacToeMatrix.DEFAULT_SYMBOL:
            return a_list.count(first_value) == len(a_list)
        else:
            return False


class TieRule(TicTacToeRule):
    def is_completed(self):
        arr = self.matrix.getA1()
        filtered_list = self.remove_values_from_list(arr,TickTacToeMatrix.DEFAULT_SYMBOL)
        return filtered_list.__len__() >= 9

    def remove_values_from_list(self,a_list, remove_value):
        return [value for value in a_list if value != remove_value]

class DiagonalRule(TicTacToeRule):
    def is_completed(self):
        return self.is_up_diagonal_complete() or self.is_down_diagonal_complete()

    def is_up_diagonal_complete(self):
        sub_list = [self.matrix[0, 2], self.matrix[1, 1], self.matrix[2, 0]]
        return self.is_symbols_equal(sub_list)

    def is_down_diagonal_complete(self):
        sub_list = [self.matrix[2, 0], self.matrix[1, 1], self.matrix[0, 2]]
        return self.is_symbols_equal(sub_list)


class HorizontalRule(TicTacToeRule):
    def is_completed(self):
        return self.is_horizontal_complete()

    def is_horizontal_complete(self):
        sub_list = []
        for h in range(self.matrix.shape[1]):
            for w in range(self.matrix.shape[0]):
                sub_list.append(self.matrix[h, w])
            if self.is_symbols_equal(sub_list):
                return True
            else:
                sub_list.clear()


class VerticalRule(TicTacToeRule):
    def is_completed(self):
        return self.is_vertical_complete()

    def is_vertical_complete(self):
        sub_list = []
        for w in range(self.matrix.shape[0]):
            for h in range(self.matrix.shape[1]):
                sub_list.append(self.matrix[h, w])
            if self.is_symbols_equal(sub_list):
                return True
            else:
                sub_list.clear()

