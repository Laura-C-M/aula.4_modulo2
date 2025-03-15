# Jogo do Galo
from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(bg='pink')
root.title("Jogo do Galo")
root.geometry("500x600")

label = Label(root, text="Jogo do Galo", font=("Times", 16))
label.grid(pady=20)

frm = ttk.Frame(root, padding=10)
frm.grid()

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1

def check_winner():
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            return states[i][0]
            # Verifica vitória na mesma linha, 0 igual a nada, 1 igual a X e 2 igual a O
        if states[0][i] == states[1][i] == states[2][i] != 0:
            return states[0][i]
            # Verifica vitória na mesma coluna, 0 igual a nada, 1 igual a X e 2 igual a O
    if states[0][0] == states[1][1] == states[2][2] != 0:
        return states[0][0]
        # Verifica vitória na diagonal principal (esq > dir), 0 igual a nada, 1 igual a X e 2 igual a O
    if states[0][2] == states[1][1] == states[2][0] != 0:
        return states[0][2]
        # Verifica vitória na diagonal secundária (dir > esq), 0 igual a nada, 1 igual a X e 2 igual a O 
    return 0
def reset_game():
    global player, states
    player = 1
    states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    label.config(text="Jogo do Galo")
    for i in range(3):
        for j in range(3):
            b[i][j].config(text="", state=NORMAL)

def clicked(r, c):
    global player
    if states[r][c] == 0:
        if player == 1:
            b[r][c].config(text="X", state=DISABLED, fg='pink')
            states[r][c] = 1
            player = 2
        else:
            b[r][c].config(text="O", state=DISABLED, fg='pink')
            states[r][c] = 2
            player = 1
        winner = check_winner()
        if winner != 0:
            label.config(text=f"Jogador {winner} venceu!")
            for i in range(3):
                for j in range(3):
                    b[i][j].config(state=DISABLED)
        elif all(states[i][j] != 0 for i in range(3) for j in range(3)):
            label.config(text="Empate! Ninguém venceu.")

# Cria os botões do jogo
for i in range(3):
    for j in range(3):
        b[i][j] = Button(frm, height=4, width=8, font=("Helvetica", 20), command=lambda r=i, c=j: clicked(r, c), fg='pink')
        b[i][j].grid(row=i, column=j)
reset_button = Button(root, text="Jogar Novamente", font=("Times", 16), command=reset_game)
reset_button.grid(pady=20)

root.mainloop()