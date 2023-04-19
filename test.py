import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


def graph():
    victoires_x = 0
    victoires_o = 0
    egalites = 0

    with open('data.csv', 'r') as graph:
        reader = csv.reader(graph)
        data = list(reader)
        graph.close()
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


graph()
