import tkinter as tk
import os
from tkinter import *
import move as mv
import play as pl

# decide player play first or ai first
def ask_multiple_choice_question(prompt, options):
    root = Tk()
    if prompt:
        Label(root, text=prompt,width = 20,height = 5,font=('Arial', 12),bg = "yellow").pack()
    v = IntVar()
    #Options
    for i, option in enumerate(options):
        Radiobutton(root, text=option, variable=v, value=i,font=('Arial', 10)).pack(anchor="w")
    Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    return options[v.get()]
result = ask_multiple_choice_question(
    "Next Game?",
    [
        "Exit",
        "AI First",
        "You First"
    ]
)

window = Tk()
if result is "AI First":
    a = pl.ttt_gui(window,'O')
    a.aiFirstMove()
elif result is "You First":
    a = pl.ttt_gui(window,'X')
else:
    os._exit(0)

#reset will cause the program restart
def reset():
    python = sys.executable
    os.execl(python, python, *sys.argv)

#reset button
restart = Button(window,text = "Restart",command = reset)
restart.grid(column=0, row=3, sticky=N + S + E + W)


window.mainloop()





