from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("TIC TAC TOE GAME")
root.geometry('850x450')

turn = ['X']

def winner():
    # Check rows
    for i in range(3):
        if b[i][0].cget('text') == b[i][1].cget('text') == b[i][2].cget('text') != '':
            msg.showinfo("Game Over", f"The winner is {b[i][0].cget('text')}")
            disable_all_buttons()
            return

    # Check columns
    for j in range(3):
        if b[0][j].cget('text') == b[1][j].cget('text') == b[2][j].cget('text') != '':
            msg.showinfo("Game Over", f"The winner is {b[0][j].cget('text')}")
            disable_all_buttons()
            return

    # Check diagonals
    if b[0][0].cget('text') == b[1][1].cget('text') == b[2][2].cget('text') != '':
        msg.showinfo("Game Over", f"The winner is {b[0][0].cget('text')}")
        disable_all_buttons()
        return
    if b[0][2].cget('text') == b[1][1].cget('text') == b[2][0].cget('text') != '':
        msg.showinfo("Game Over", f"The winner is {b[0][2].cget('text')}")
        disable_all_buttons()
        return

    # Check for draw
    if all(b[i][j].cget('text') != '' for i in range(3) for j in range(3)):
        msg.showinfo("Game Over", "It's a Draw!")
        return

def click(r, c):
    if b[r][c].cget('text') == '':
        b[r][c].config(text=turn[0], state='disabled')
        turn[0] = 'O' if turn[0] == 'X' else 'X'
        winner()

def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state='disabled')

def reset_game():
    for i in range(3):
        for j in range(3):
            b[i][j].config(text='', state='normal')
    turn[0] = 'O' 

# Frames
f1 = Frame(root)
f1.grid(padx=180)
f2 = Frame(root)
f2.grid(padx=180, pady=20)
f3 = Frame(root)
f3.grid(padx=180, pady=30)

Label(f1, text="WELCOME TO TIC TAC TOE GAME", font=('Arial', 16)).grid()

# Buttons Grid
b = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(f2, text='', height=6, width=20, bg='white', fg='black',
                         command=lambda r=i, c=j: click(r, c))
        b[i][j].grid(row=i, column=j)

# Reset Button
Button(f3, text='Reset', width=40, bg='orange', height=2, command=reset_game).grid()

root.mainloop()