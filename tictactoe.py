import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("135x180")
        self.create_widgets()
        self.turn = "X"

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, width=5, height=2, command=lambda i=i: self.play(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=3)

        new_game_button = tk.Button(self.root, text="New game", command=self.new_game)
        new_game_button.grid(row=4, column=0, columnspan=3)

    def play(self, index):
        button = self.buttons[index]
        button.config(text=self.turn, state="disabled")
        self.check_game_status()
        self.switch_turn()

    def new_game(self):
        self.turn = "X"
        for button in self.buttons:
            button.config(text="", state="normal")
            self.result_label.config(text="")

    def switch_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
        
    def check_game_status(self):
        # Check for win or loss
        win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in win:
            if self.buttons[i[0]]['text'] == self.buttons[i[1]]['text'] == self.buttons[i[2]]['text'] and self.buttons[i[0]]['text'] != "":
                self.result_label.config(text="Player {} wins!".format(self.buttons[i[0]]['text']))
                self.disable_all_buttons()
                return
        if self.is_draw():
            self.result_label.config(text="It's a draw!")
            self.disable_all_buttons()
            return
    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def is_draw(self):
        # Check for draw
        for button in self.buttons:
            if button['text'] == "":
                return False
        return True
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()
