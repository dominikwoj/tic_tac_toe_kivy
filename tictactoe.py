class TicTacToe:
    def __init__(self):
        self.__moves_table = [[None] * 3, [None] * 3, [None] * 3]
        self.__keys_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.__players = 'XO'
        self.__player = None
        self.__player_won = False
        self.__place_array = lambda x: int(x) - 1
        self.__wrong_turn = False
        self.__set_player()

    def get_status(self):
        print(f'{self.__moves_table}|{self.__wrong_turn}|{self.__player}|{self.__player_won}')
        return {'wrong_turn': self.__wrong_turn, 'turn': self.__player, 'winner': self.__player_won}

    def __set_player(self):
        self.__player = self.__players[0] if self.__player == None else \
            self.__players[1] if self.__player == self.__players[0] else self.__players[0]

    def __put_marker(self, _place, _row):
        if self.__moves_table[_row][_place] == None:
            self.__moves_table[_row][_place] = self.__player
            if self.__check_if_player_win() is True:
                self.__player_won = True
            else:
                self.__set_player()
        else:
            self.__wrong_turn = True

    def __check_if_player_win(self):
        p = self.__player
        mt = self.__moves_table
        return any([all(i == p for i in [mt[0][0], mt[0][1], mt[0][2]]),
                    all(i == p for i in [mt[1][0], mt[1][1], mt[1][2]]),
                    all(i == p for i in [mt[2][0], mt[2][1], mt[2][2]]),
                    all(i == p for i in [mt[0][0], mt[1][0], mt[2][0]]),
                    all(i == p for i in [mt[0][1], mt[1][1], mt[2][1]]),
                    all(i == p for i in [mt[0][2], mt[1][2], mt[2][2]]),
                    all(i == p for i in [mt[0][0], mt[1][1], mt[2][2]]),
                    all(i == p for i in [mt[0][2], mt[1][1], mt[2][0]]),
                    ])

    def turn(self, place):
        self.__wrong_turn = False
        match place:
            case place if place in '123':
                self.__put_marker(self.__place_array(place), 0)
            case place if place in '456':
                self.__put_marker(self.__place_array(place) - 3, 1)
            case place if place in '789':
                self.__put_marker(self.__place_array(place) - 6, 2)