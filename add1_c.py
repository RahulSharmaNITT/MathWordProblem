from tkinter import *
from PIL import ImageTk, Image
import os
import sys 
root = Tk()
root.minsize(300,100)
root.geometry("1560x768")
root.title("Mathword_Problem_Hints")
root.configure(background="#99ccff")


def call1():
    root.destroy()
    os.system("python Home.py")
 
def call2():
    root.destroy()
    os.system("python add1.py")
 
def call3():
    root.destroy()
 
photo1=PhotoImage(file="home2.png")
b = Button(root,image=photo1, font=('arial', 15, 'bold'), bd=16,bg="#012b74", fg="white", text="HOME", command=call1, height=128, width=220, compound=LEFT)
b.place(x = 40, y = 20)

photo2=PhotoImage(file="next3.png")
b = Button(root,image=photo2, font=('arial', 15, 'bold'), bd=16,bg="#012b74", fg="white", text="NEXT", command=call2, height=128, width=220, compound=LEFT)
b.place(x = 40, y = 240)

photo3=PhotoImage(file="exit.png")
b = Button(root,image=photo3, font=('arial', 15, 'bold'), bd=16,bg="#012b74", fg="white", text="EXIT", command=call3, height=128, width=220, compound=LEFT)
b.place(x = 40, y = 460)


photo4=PhotoImage(file="ay36.png")
b = Button(root,image=photo4, font=('arial', 15, 'bold'), bd=16,bg="#012b74", fg="white", height=570, width=530, compound=LEFT)
b.place(x = 370, y = 20)

photo5=ImageTk.PhotoImage(Image.open("boy.jpg"))
b = Button(root,image=photo5, font=('arial', 15, 'bold'),bd=8 ,bg="#012b74", fg="white",height=580, width=250, compound=LEFT)
b.place(x = 1000, y = 20)

mainloop()
