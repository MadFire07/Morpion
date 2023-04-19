import tkinter as tk

window = tk.Tk()
window.title("Morpion")
window.configure(background='white')
window.geometry("1200x900")
titre = tk.Label(window, text="Morpion", font=("Arial", 30, "bold"), bg="white", fg="black", width=20, height=3)
titre.grid(row=0, column=0, columnspan=3, padx=200, pady=5)

largGrl = 600
hautGrl = 600
grille = tk.Canvas(window, width=largGrl, height=hautGrl, bg="grey")
grille.grid(row=1, column=0, padx=150)

for i in range(0, 401, 200):
    grille.create_line(i, 10, i, 590, width=5)
    grille.create_line(10, i, 590, i, width=5)

terminate = tk.Button(window, text="Quitter", font=("Arial", 20, "bold"), bg="white", fg="black", width=20, height=2,
                      command=window.destroy)
terminate.grid(row=2, column=0, columnspan=3, padx=0, pady=10)


def clic(event):
    position = 0
    x = event.x
    y = event.y
    if 0 < x < 200 and 0 < y < 200:
        grille.create_line(30, 30, 170, 170, width=10, fill="red")
        grille.create_line(170, 30, 30, 170, width=10, fill="red")
        position = 1
    elif 400 > x > 200 > y > 0:
        grille.create_line(230, 30, 370, 170, width=10, fill="red")
        grille.create_line(370, 30, 230, 170, width=10, fill="red")
        position = 2
    elif 400 < x < 600 and 0 < y < 200:
        grille.create_line(430, 30, 570, 170, width=10, fill="red")
        grille.create_line(570, 30, 430, 170, width=10, fill="red")
        position = 3
    elif 0 < x < 200 < y < 400:
        grille.create_line(30, 230, 170, 370, width=10, fill="red")
        grille.create_line(170, 230, 30, 370, width=10, fill="red")
        position = 4
    elif 200 < x < 400 and 200 < y < 400:
        grille.create_line(230, 230, 370, 370, width=10, fill="red")
        grille.create_line(370, 230, 230, 370, width=10, fill="red")
        position = 5
    elif 600 > x > 400 > y > 200:
        grille.create_line(430, 230, 570, 370, width=10, fill="red")
        grille.create_line(570, 230, 430, 370, width=10, fill="red")
        position = 6
    elif 0 < x < 200 and 400 < y < 600:
        grille.create_line(30, 430, 170, 570, width=10, fill="red")
        grille.create_line(170, 430, 30, 570, width=10, fill="red")
        position = 7
    elif 200 < x < 400 < y < 600:
        grille.create_line(230, 430, 370, 570, width=10, fill="red")
        grille.create_line(370, 430, 230, 570, width=10, fill="red")
        position = 8
    elif 400 < x < 600 and 400 < y < 600:
        grille.create_line(430, 430, 570, 570, width=10, fill="red")
        grille.create_line(570, 430, 430, 570, width=10, fill="red")
        position = 9
    return position

print(clic)

grille.bind("<Button-1>", clic)

window.mainloop()
