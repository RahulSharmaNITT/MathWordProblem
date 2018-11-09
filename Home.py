from tkinter import *
import random
import time
import os
from PIL import ImageTk, Image

root=Tk()
root.geometry("1500x600")
root.title("Mathword_Problem_Home")
root.configure(background="#99ccff")

text_Input=StringVar()

def OnDoubleab(evt):
     os.system("python notepad.py")

def OnDoubleba(evt):
     os.system("python notepad.py")     

def OnDouble1(Event):
     root.destroy()
     os.system("python add1.py")
     
def OnDouble2(evt):
     root.destroy()
     os.system("python add2.py")

def OnDouble3(evt):
     root.destroy()
     os.system("python add3.py")

def OnDouble4(evt):
     root.destroy()
     os.system("python sub1.py")

def OnDouble5(evt):
     root.destroy()
     os.system("python sub2.py")

def OnDouble6(evt):
     root.destroy()
     os.system("python sub3.py")

def OnDouble7(evt):
     root.destroy()
     os.system("python mul1.py")

def OnDouble8(evt):
     root.destroy()
     os.system("python mul2.py")

def OnDouble9(evt):
     root.destroy()
     os.system("python mul3.py")
     
def OnDouble10(evt):
     root.destroy()
     os.system("python div1.py")

def OnDouble11(evt):
     root.destroy()
     os.system("python div2.py")
     
def OnDouble12(evt):
     root.destroy()
     os.system("python div3.py")     
     

     
Tops=Frame(root,width=900,height=500, bg="#99ccff", relief=SUNKEN)
Tops.pack(side=TOP)

#left side option frame
f1=Frame(root,width=600,height=300, bg="#99ccff", relief=SUNKEN)
f1.pack(side=LEFT)

#right side option frame
f2=Frame(root,width=600,height=300, bg="#99ccff", relief=SUNKEN)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lblinfo=Label(Tops,font=('aldhabi',30,'bold'),text="Question Generator For Mathword Problem",fg="white", bg='#99ccff', bd=4, anchor='w')
lblinfo.grid(row=0,column=0)


#Mathword Problem starting
listboxa1 = Listbox(f1,font=('algerian',15,'bold'),bg="white",bd=4, fg="#012b74", height=2, width=25)
listboxa1.insert(END, "  Mathword Problem:-")
listboxa1.pack()

listboxa2 = Listbox(f1,font=('algerian',15,'bold'),bg="#f3ce13",bd=4, fg="#012b74", height=2, width=25)
listboxa2.insert(END, " 1. ADDITION:-")
listboxa2.pack()

listboxa = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxa.insert(END, "   1.1-Initial value unknown")
listboxa.bind("<<ListboxSelect>>", OnDouble1)
listboxa.pack()

listboxb = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxb.insert(END, "   1.2-Change value unknown")
listboxb.bind("<<ListboxSelect>>", OnDouble2)
listboxb.pack()

listboxc = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxc.insert(END, "   1.3-Result value unknown")
listboxc.bind("<<ListboxSelect>>", OnDouble3)
listboxc.pack()

listboxd1 = Listbox(f1,font=('algerian',15,'bold'),bg="#f3ce13",bd=4, fg="#012b74", height=2, width=25)
listboxd1.insert(END, " 2. SUBTRACTION:-")
listboxd1.pack()

listboxd = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxd.insert(END, "   2.1-Initial value unknown")
listboxd.bind("<<ListboxSelect>>", OnDouble4)
listboxd.pack()

listboxe = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxe.insert(END, "   2.2-Change value unknown")
listboxe.bind("<<ListboxSelect>>", OnDouble5)
listboxe.pack()

listboxf = Listbox(f1,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxf.insert(END, "   2.3-Result value unknown")
listboxf.bind("<<ListboxSelect>>", OnDouble6)
listboxf.pack()
#right side

listbox1a = Listbox(f2,font=('algerian',15,'bold'),bg="white",bd=4, fg="#012b74", height=2, width=25)
listbox1a.insert(END, "   Mathword Problem:-")
listbox1a.pack()

listboxg1 = Listbox(f2,font=('algerian',15,'bold'),bg="#f3ce13",bd=4, fg="#012b74", height=2, width=25)
listboxg1.insert(END, " 3. MULTIPLICATION:-")
listboxg1.pack()

listboxg = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxg.insert(END, "   3.1-Initial value unknown")
listboxg.bind("<<ListboxSelect>>", OnDouble7)
listboxg.pack()

listboxh = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxh.insert(END, "   3.2-Change value unknown")
listboxh.bind("<<ListboxSelect>>", OnDouble8)
listboxh.pack()

listboxi = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxi.insert(END, "   3.3-Result value unknown")
listboxi.bind("<<ListboxSelect>>", OnDouble9)
listboxi.pack()

listboxj1 = Listbox(f2,font=('algerian',15,'bold'),bg="#f3ce13",bd=4, fg="#012b74", height=2, width=25)
listboxj1.insert(END, " 4. DIVISION:-")
listboxj1.pack()

listboxj = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxj.insert(END, "   4.1-Initial value unknown")
listboxj.bind("<<ListboxSelect>>", OnDouble10)
listboxj.pack()

listboxk = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxk.insert(END, "   4.2-Change value unknown")
listboxk.bind("<<ListboxSelect>>", OnDouble11)
listboxk.pack()

listboxl = Listbox(f2,font=('arial',15,'bold'),bg="#01b9f5",bd=4, fg="#012b74", height=2, width=30)
listboxl.insert(END, "   4.3-Result value unknown")
listboxl.bind("<<ListboxSelect>>", OnDouble12)
listboxl.pack()

#centre image
img = ImageTk.PhotoImage(Image.open("front5.jpg"))
panel = Label(root, image = img, bg="#99ccff")
panel.pack(side = "bottom", fill = "both", expand = "yes")



#scrollbar1.config( command = listbox1.yview)

root.mainloop()
