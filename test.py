import tkinter as tk

class MorpionUI:
    def init(self, master, on_click):
        self.master = master
        self.on_click = on_click

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text='', width=10, height=3,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def update_button(self, index, text):
        self.buttons[index].config(text=text, state='disabled')

    def settitle(self, title):
        self.master.title(title)

class Morpion:
    def init(self, master):
        self.master = master
        self.master.title("Morpion")
        self.master.resizable(False, False)

        self.turn = 'X'
        self.board = ['' for  in range(9)]
        self.ui = MorpionUI(self.master, self.on_click)

    def on_click(self, index):
        if self.board[index] == '' and not self.game_over():
            self.ui.update_button(index, self.turn)
            self.board[index] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'

            if self.game_over():
                self.ui.set_title("Morpion - Fin de la partie")

    def game_over(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for a, b, c in winning_combinations:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return True

        if all(cell != '' for cell in self.board):
            return True

        return False

def main():
    root = tk.Tk()
    Morpion(root)
    root.mainloop()

if __name__ == 'main':
    main()