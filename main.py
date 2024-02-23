from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from tictactoe import TicTacToe


class TheLabApp(GridLayout):
    def __init__(self, **kwargs):
        super(TheLabApp, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 5
        self.buttons = []
        self.ttt = TicTacToe()

        for i in range(9):
            button = Button(text="")
            self.buttons.append(button)
            self.add_widget(button)
        self.children[0].bind(on_press=lambda *args: self.button_click('9', *args))
        self.children[1].bind(on_press=lambda *args: self.button_click('8', *args))
        self.children[2].bind(on_press=lambda *args: self.button_click('7', *args))
        self.children[3].bind(on_press=lambda *args: self.button_click('6', *args))
        self.children[4].bind(on_press=lambda *args: self.button_click('5', *args))
        self.children[5].bind(on_press=lambda *args: self.button_click('4', *args))
        self.children[6].bind(on_press=lambda *args: self.button_click('3', *args))
        self.children[7].bind(on_press=lambda *args: self.button_click('2', *args))
        self.children[8].bind(on_press=lambda *args: self.button_click('1', *args))
        # print(f'children_count={len(self.children)}')
        # for i in range(len(self.children)):
        #     print(i, self.children[i])
        #     self.children[i].bind(on_press=lambda *args: self.button_click(str(len(self.children)-i), *args))

        box_layout = BoxLayout()
        self.label = Label(text=f"Turn: {self.ttt.get_status()['turn']}")
        box_layout.add_widget(self.label)
        self.add_widget(box_layout)

    def button_click(self, event, handler):
        print(event, handler)
        status_game = self.ttt.get_status()
        turn_b, winner = status_game['turn'], status_game['winner']
        if winner is False:
            self.ttt.turn(event)
            status_game = self.ttt.get_status()
            turn_n, winner, wrong_turn = status_game['turn'], status_game['winner'], status_game['wrong_turn']
            if winner is True:
                handler.text = turn_b
                self.label.text = f"Winner:{turn_b}!!! Game over."
            elif wrong_turn is False:
                handler.text = turn_b
                self.label.text = f"Turn: {turn_n}"
            else:
                self.label.text = f"Wrong turn! Turn:{turn_n}"

class MyApp(App):
    def build(self):
        self.title = 'Tic-Tac-Toe designed by Dominik Wojnowski'
        return TheLabApp()


if __name__ == '__main__':
    MyApp().run()
