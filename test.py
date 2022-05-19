
from asyncio import events
import tkinter as tk


root = tk.Tk()
root.title("〇×ゲーム")


w = 30
h = 10


def player_judge(event):
    event.wiget["textvariable"] = "maru"


button1 = tk.Button(root, width=w, height=h, bg="red")
button2 = tk.Button(root, width=w, height=h,  bg="blue")
button3 = tk.Button(root, width=w, height=h)
button4 = tk.Button(root, width=w, height=h)
button5 = tk.Button(root, width=w, height=h)
button6 = tk.Button(root, width=w, height=h)
button7 = tk.Button(root, width=w, height=h)
button8 = tk.Button(root, width=w, height=h)
button9 = tk.Button(root, width=w, height=h)


button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=0, column=3)
button4.grid(row=1, column=1)
button5.grid(row=1, column=2)
button6.grid(row=1, column=3)
button7.grid(row=2, column=1)
button8.grid(row=2, column=2)
button9.grid(row=2, column=3)

root.bind("<1>", player_judge)


root.mainloop()
