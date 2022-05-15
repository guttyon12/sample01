import tkinter as tk

root = tk.Tk()
root.title("〇×ゲーム")

canvas = tk.Canvas(width=800, height=700,)
canvas.pack()

frame = tk.Frame(root)
frame.place()
"""
button1 = tk.Button(root, widht=20, height=20)
button2 = tk.Button(root, widht=20, height=20)
button3 = tk.Button(root, widht=20, height=20)
button4 = tk.Button(root, widht=20, height=20)
button5 = tk.Button(root, widht=20, height=20)
button6 = tk.Button(root, widht=20, height=20)
button7 = tk.Button(root, widht=20, height=20)
button8 = tk.Button(root, width=20, height=20)
button9 = tk.Button(root, width=20, height=20)

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=2, row=0)
button4.grid(column=0, row=1)
button5.grid(column=1, row=1)
button6.grid(column=2, row=1)
button7.grid(column=0, row=2)
button8.grid(column=1, row=2)
button9.grid(column=2, row=2)
"""

root.mainloop()
