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
    # Vérifie si le joueur 1 a gagné, retourne -1
    if check_win(board, 1):
        return -1
    # Vérifie si le joueur 2 a gagné, retourne 1
    elif check_win(board, 2):
        return 1
    # Vérifie si le plateau est plein, retourne 0 pour un match nul
    elif all([x != 0 for row in board for x in row]):
        return 0

    if maximizing_player:
        # Initialisation du score maximal à -infini
        max_eval = float('-inf')
        # Parcourt chaque case du plateau de jeu
        for i in range(3):
            for j in range(3):
                # Vérifie si la case est vide
                if board[i][j] == 0:
                    # Place le symbole du joueur maximisant dans la case
                    board[i][j] = 2
                    # Appelle récursivement la fonction minimax avec le plateau mis à jour
                    # et le joueur suivant (minimisant)
                    eval = minimax(board, depth + 1, False)
                    # Réinitialise la case à sa valeur d'origine
                    board[i][j] = 0
                    # Met à jour le score maximal
                    max_eval = max(max_eval, eval)
        # Retourne le score maximal trouvé
        return max_eval
    else:
        # Initialisation du score minimal à +infini
        min_eval = float('inf')
        # Parcourt chaque case du plateau de jeu
        for i in range(3):
            for j in range(3):
                # Vérifie si la case est vide
                if board[i][j] == 0:
                    # Place le symbole du joueur minimisant dans la case
                    board[i][j] = 1
                    # Appelle récursivement la fonction minimax avec le plateau mis à jour
                    # et le joueur suivant (maximisant)
                    eval = minimax(board, depth + 1, True)
                    # Réinitialise la case à sa valeur d'origine
                    board[i][j] = 0
                    # Met à jour le score minimal
                    min_eval = min(min_eval, eval)
        # Retourne le score minimal trouvé
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
    global current_player  # utilise la variable globale 'current_player'
    if board[row][col] == 0:  # si la case est vide
        board[row][col] = current_player  # met le symbole du joueur courant sur la case
        if current_player == 1:  # si c'est le joueur 1
            button[row][col].configure(text="X", fg="red")  # configure le texte et la couleur de la case
            if check_win(board, current_player):  # vérifie si le joueur a gagné
                messagebox.showinfo("Victoire", f"Le joueur {current_player} a gagné !")  # affiche un message de victoire
                save_game(current_player)  # sauvegarde la partie
                return  # termine la fonction
            elif all([x != 0 for row in board for x in row]):  # vérifie si toutes les cases sont remplies
                messagebox.showinfo("Match nul", "Match nul !")  # affiche un message de match nul
                save_game(0)  # sauvegarde la partie
                return  # termine la fonction
            else:  # si la partie n'est pas terminée
                current_player = 3 - current_player  # change de joueur
                ai_move = best_move(board)  # l'ordinateur joue
                if ai_move:  # si l'ordinateur a trouvé un coup valide
                    board[ai_move[0]][ai_move[1]] = current_player  # met le symbole de l'ordinateur sur la case
                    button[ai_move[0]][ai_move[1]].configure(text="O", fg="blue")  # configure le texte et la couleur de la case
                    if check_win(board, current_player):  # vérifie si l'ordinateur a gagné
                        messagebox.showinfo("Victoire", f"L'Ordinateur a gagné !")  # affiche un message de victoire
                        save_game(current_player)  # sauvegarde la partie
                        return  # termine la fonction
                    elif all([x != 0 for row in board for x in row]):  # vérifie si toutes les cases sont remplies
                        messagebox.showinfo("Match nul", "Match nul !")  # affiche un message de match nul
                        save_game(0)  # sauvegarde la partie
                        return  # termine la fonction
                current_player = 3 - current_player  # change de joueur



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
