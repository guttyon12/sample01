
from cgitb import text
import tkinter
import sys
from tkinter import *
from tkinter import ttk
from turtle import right

def maru(left_up,right_down):
    ##canvas.create_oval(left_up,left_up,right_down,right_down)
    return 0

def batu(left_up,right_down):
    ##canvas.create_line(left_up,left_up,right_down,right_down)
    ##canvas.create_line(left_up + 80,left_up,right_down - 80 ,right_down)
    return 0


root = tkinter.Tk()
root.title(u"maru")
root.geometry("500x500")

label = tkinter.Label(root, text="〇×ゲーム")
label.pack()

canvas = tkinter.Canvas(root, width= 400, height= 400)
canvas.place(x=0, y=0)
##canvas.create_oval(10,10,140,140, fill="red")
canvas.create_line(200,100,200,400)
canvas.create_line(300,100,300,400)

canvas.create_line(100,200,400,200)
canvas.create_line(100,300,400,300)

left_up_button = tkinter.Button(root, command = maru(110,110), text="test")
left_up_button.place(150,150)







root.mainloop()
