from tkinter import *
from random import randrange

root = Tk()
app_size = "640x480"
root.geometry(app_size)
root.resizable(height=False, width=False)

dice_roll = 0

roll_label = Label(root, text=dice_roll, font="None, 100")



def update():
	roll_label.config(text=dice_roll)

def roll(sides):
	global dice_roll
	dice_roll = randrange(1, sides + 1)
	update()



six_button = Button(root, text="6 Sided Dice", command=lambda:roll(6))
ten_button = Button(root, text="10 Sided Dice", command=lambda:roll(10))
twenty_button = Button(root, text="20 Sided Dice", command=lambda:roll(20))



six_button.place(x=20, y=20, anchor=NW)
ten_button.place(x=250, y=20, anchor=NW)
twenty_button.place(x=500, y=20, anchor=NW)

roll_label.place(x=300, y=200, anchor=NW)





root.mainloop()