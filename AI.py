from main import check_win
import pandas as pd
import numpy as np


def get_data():
    data = pd.read_csv('data.csv')
    return data

def possible_moves(data):
    moves = []
    for i in range(9):
        if data[i] == 0:
            moves.append(i)
    return moves

print(get_data())