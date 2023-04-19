import tkinter as tk
from tkinter import messagebox
import csv
import pandas as pd
import matplotlib.pyplot as plt


# Fonction pour vérifier si un joueur a gagné
def check_win(board, player):
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


def minimax(board, depth, maximizing_player):
    if check_win(board, 1):
        return -1
    elif check_win(board, 2):
        return 1
    elif all([x != 0 for row in board for x in row]):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
        return min_eval


def best_move(board):
    max_eval = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                eval = minimax(board, 0, False)
                board[i][j] = 0
                if eval > max_eval:
                    max_eval = eval
                    move = (i, j)
    return move


# Fonction pour gérer le clic sur une case
def on_click(row, col):
    global current_player
    if board[row][col] == 0:
        board[row][col] = current_player
        if current_player == 1:
            button[row][col].configure(text="X", fg="red")
            if check_win(board, current_player):
                messagebox.showinfo("Victoire", f"Le joueur {current_player} a gagné !")
                save_game(current_player)
                return
            elif all([x != 0 for row in board for x in row]):
                messagebox.showinfo("Match nul", "Match nul !")
                save_game(0)
                return
            else:
                current_player = 3 - current_player
                ai_move = best_move(board)
                if ai_move:
                    board[ai_move[0]][ai_move[1]] = current_player
                    button[ai_move[0]][ai_move[1]].configure(text="O", fg="blue")
                    if check_win(board, current_player):
                        messagebox.showinfo("Victoire", f"Le joueur {current_player} a gagné !")
                        save_game(current_player)
                        return
                    elif all([x != 0 for row in board for x in row]):
                        messagebox.showinfo("Match nul", "Match nul !")
                        save_game(0)
                        return
                current_player = 3 - current_player


# Fonction pour réinitialiser le jeu
def reset_game():
    global current_player, board
    current_player = 1
    board = [[0] * 3 for _ in range(3)]
    pd.DataFrame(board)
    for i in range(3):
        for j in range(3):
            button[i][j].configure(text="", state="normal")


def graphics():
    # Créer une fenêtre Tkinter
    global window, button
    window = tk.Tk()
    window.title("Morpion")

    # Créer un titre pour la fenêtre
    title = tk.Label(window, text="Morpion", font=("Arial", 20))
    title.grid(row=0, column=0, columnspan=3, pady=2)

    # Créer une grille de boutons pour représenter le morpion
    button = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            button[i][j] = tk.Button(window, text="", width=4, height=2, font=("Arial", 80),
                                     command=lambda row=i, col=j: on_click(row, col))
            button[i][j].grid(row=i, column=j)

    # Créer un bouton pour réinitialiser le jeu

    reset_button = tk.Button(window, text="Restart", width=10, height=2, command=reset_game)
    reset_button.grid(row=3, column=0, columnspan=3, pady=2)

    # Créer un bouton pour quitter le jeu

    quit_button = tk.Button(window, text="Quit", width=10, height=2, command=window.destroy)
    quit_button.grid(row=4, column=0, columnspan=3, pady=2)

    # Créer un bouton pour afficher les statistiques

    stats_button = tk.Button(window, text="Stats", width=10, height=2, command=graph)
    stats_button.grid(row=5, column=0, columnspan=3, pady=2)


# mettre le resultat de la partie dans un fichier csv
def save_game(winner):
    print(winner)
    database = board + [str(winner)]
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(database)
        csvfile.close()


def graph():
    global victoires_x, victoires_o, egalites
    victoires_x = 0
    victoires_o = 0
    egalites = 0

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        file.close()
    for ligne in data:
        result = ligne[3]
        if result == str(1):
            victoires_x += 1
        elif result == str(2):
            victoires_o += 1
        elif result == str(0):
            egalites += 1

    total_victoires = victoires_x + victoires_o + egalites
    x = ['X', 'O', 'Égalités']
    y = [victoires_x / total_victoires * 100, victoires_o / total_victoires * 100, egalites / total_victoires * 100]
    colors = ['red', 'blue', 'green']

    plt.bar(x, y, color=colors)
    plt.xlabel("Joueur")
    plt.ylabel("Pourcentage de victoires")
    plt.title("Comparaison des victoires entre X et O (en pourcentage)")
    plt.show()


# Initialiser le jeu

graphics()
reset_game()

# Lancer la boucle principale Tkinter

window.mainloop()
