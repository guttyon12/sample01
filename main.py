import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox


def init_data():
    global init, data
    data = [[init for i in range(3)] for j in range(3)]


def check(e):
    global data, player
    for i in range(3):
        for j in range(3):
            if e.widget == btn[j][i]:
                if player == 1:
                    e.widget["text"] = "〇"
                    data[j][i] = 1
                elif player == -1:
                    e.widget["text"] = "×"
                    data[j][i] = -1

    player = turn()

    if judge() == 1:
        messagebox.showinfo('ゲーム終了', "先行の勝利")
        init_data()
        init_text()
    elif judge() == -1:
        messagebox.showinfo('ゲーム終了', "後攻の勝利")
        init_data()
        init_text()
    elif judge() == -2:
        messagebox.showinfo('ゲーム終了', "引き分け")
        init_data()
        init_text()


def judge():
    global data
    # 縦の探索
    for i in range(3):
        if data[i][0] != 0:
            if data[i][0] == data[i][1] and data[i][0] == data[i][2]:
                return data[i][0]

    # 横の探索
    for j in range(3):
        if data[0][j] != 0:
            if data[0][j] == data[1][j] and data[0][j] == data[2][j]:
                return data[0][j]

    # 斜めの探索
    if data[1][1] != 0:
        if data[0][0] == data[1][1] and data[0][0] == data[2][2]:
            return data[1][1]
        elif data[0][2] == data[1][1] and data[0][2] == data[2][0]:
            return data[1][1]

    for i in range(3):
        for j in range(3):
            if data[j][i] == 0:
                return 0

    return -2

# プレイヤーの変更


def turn():
    global player
    return player * (-1)


def init_text():
    global btn
    for i in range(3):
        for j in range(3):
            btn[i][j]["text"] = ""


root = tk.Tk()
root.title("〇×ゲーム")

player = 1

init = 0
data = [[init for i in range(3)] for j in range(3)]

w = 30
h = 10

btn = [[tk.Button(root, width=w, height=h) for i in range(3)]
       for j in range(3)]

for i in range(3):
    for j in range(3):
        btn[j][i].grid(column=j, row=i)


root.bind("<ButtonPress>", check)

root.mainloop()
