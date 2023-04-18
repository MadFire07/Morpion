import tkinter as tk
from tkinter import messagebox


# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    for i in range(3):
        # Vérifier les rangées
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Vérifier les colonnes
        elif board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Vérifier les diagonales
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Fonction pour gérer le clic sur une case
def on_click(row, col):
    global current_player
    if board[row][col] == 0:
        board[row][col] = current_player
        if current_player == 1:
            button[row][col].configure(text="X")
        else:
            button[row][col].configure(text="O")
        if check_win(current_player):
            messagebox.showinfo("Victoire", f"Le joueur {current_player} a gagné !")
            reset_game()
        elif all([x != 0 for row in board for x in row]):
            messagebox.showinfo("Match nul", "Match nul !")
            reset_game()
        else:
            current_player = 3 - current_player


# Fonction pour réinitialiser le jeu
def reset_game():
    global current_player, board
    current_player = 1
    board = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            button[i][j].configure(text="", state="normal")


# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Morpion")

# Créer une grille de boutons pour représenter le morpion
button = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        button[i][j] = tk.Button(window, text="", width=5, height=2, font=("Arial", 20),
                                 command=lambda row=i, col=j: on_click(row, col))
        button[i][j].grid(row=i, column=j)

# Initialiser le jeu
reset_game()

# Lancer la boucle principale Tkinter
window.mainloop()
