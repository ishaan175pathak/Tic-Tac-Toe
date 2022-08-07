import tkinter as tk
from tkinter import messagebox
from tkinter.constants import DISABLED, NORMAL
from tkinter.messagebox import showinfo
import random as r

#################################################################################

def change_turn():
    global turn

    for t in ['X','O']:
        if not(t == turn):
            turn = t
            break

def reset():
    global turn
    for i in range(3):
        for j in range(3):
            b[i][j]["text"]=" "
            b[i][j]["state"] = NORMAL
            b[i][j]["background"] = "lightyellow"

    turn = r.choice(['X','O'])


def check_win():
    global turn

    for i in range(3):
        if (b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==turn or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==turn):
            messagebox.showinfo("Win",f"{turn} Won")
            reset()
        elif(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==turn or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==turn):
            messagebox.showinfo("Win", f"{turn} Won")
            reset()
        elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
            messagebox.showinfo("Tied",f"Match Tied")
            reset()    

def isfull():
    for i in range(3):
        for j in range(3):
            if(b[i][j]["text"] == " "):
                return False
    
    return True

def chance(row,col):
    global turn
    b[row][col].config(text=turn,bg="lightblue",state=DISABLED)
    check_win()
    if not(isfull()):
        change_turn()
        l1.config(text=turn+"'s Turn")
    elif isfull():
        l1.config(text="Match Tied ")
    

def button(frame):
    return tk.Button(frame,padx=5,width=5,text=" ",font=("arial",40,"bold"),bg="lightyellow",relief="sunken",bd=10)

#################################################################################

Main = tk.Tk()
Main.title("TIc Tac Toe")
Main.geometry("650x500")
Main.maxsize(650,500)
Main.minsize(650,500)
turn = r.choice(["X","O"])

l1 = tk.Label(Main,text="Chance of "+turn+"!")
l1.grid(row=3,column=0,columnspan=3)

b = [[],[],[]]

for i in range(3):
    for j in range(3):
        b[i].append(button(Main))
        b[i][j].config(command=lambda row=i,col=j:chance(row,col))
        b[i][j].grid(row=i,column=j)

b1 = tk.Button(Main,text="Reset",bg="lightblue",command=reset)
b1.grid(row=4,column=2)

Main.mainloop()