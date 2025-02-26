from tkinter import *
from tkinter import messagebox

global D, x1, x2, x

def Graafik():
    pass

def entryColor(event):
    i=lbl_a.get()
    if i == "":
        lbl_a.configure(bg="red")
    else:
        lbl_a.configure(bg="#ffe6f0")

    i=lbl_b.get()
    if i == "":
        lbl_b.configure(bg="red")
    else:
        lbl_b.configure(bg="#ffe6f0")
    i=lbl_c.get()
    if i == "":
        lbl_c.configure(bg="red")
    else:
        lbl_c.configure(bg="#ffe6f0")

def Solve():
    try:
        a = float(lbl_a.get())
        b = float(lbl_b.get())
        c = float(lbl_c.get())

        D = b**2 - 4* a * c

        if D>0:
            x1=round((-b+(D**(1/2)))/(2*a),2)
            x2=round((-b-(D**(1/2)))/(2*a),2)
            lbl_vastus.configure(text=f"D > 0 --> 2 решения: \n x1 = {x1}\n x2 = {x2}")

        elif D == 0:
            x =round((-b / (2*a)), 2)
            lbl_vastus.configure(text=f"D = 0 --> 1 решение: \n x = {x}")


        else:
            lbl_vastus.configure(text="Решений нет")
        
    except:
        messagebox.showerror("error", 
        """ 
             /\_/\  
            ( ╬ಠ益ಠ)  
            ( つ ϞϞ  
        """)

# aken=Tk()
# aken.geometry("650x260")
# aken.resizable(False,False)
# aken.title("Ruutvõrrand")
# f1=Frame(aken,width=650,height=260)
# f1.pack()
# lbl=Label(f1,text="Ruutvõrrandite lahendus",font="Calibri 26",fg="green",bg="lightblue")
# lbl.pack(side=TOP)
# lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
# lbl_vastus.pack(side=BOTTOM)

# lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
# lbl_a.pack(side=LEFT)
# lbl_a.bind("<KeyRelease>" ,entryColor)

# x2=Label(f1,text="x^2+",font="Calibri 26",fg="green",padx=10)
# x2.pack(side=LEFT)

# lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
# lbl_b.pack(side=LEFT)
# lbl_b.bind("<KeyRelease>" ,entryColor)

# x=Label(f1,text="x+",font="Calibri 26",fg="green",padx=10)
# x.pack(side=LEFT)

# lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
# lbl_c.pack(side=LEFT)
# lbl_c.bind("<KeyRelease>" ,entryColor)

# y=Label(f1,text="=0",font="Calibri 26",fg="green",padx=10)
# y.pack(side=LEFT)
# btn_lahenda=Button(f1,text="Lahenda",font="Calibri 26",fg="green",command=Solve)
# btn_lahenda.pack(side=LEFT)
# btn_graafik=Button(f1,text="Graafik",font="Calibri 26",fg="green",command=Graafik)
# btn_graafik.pack(side=LEFT)
    
# aken.mainloop()



def Aken_grid():
    global lbl_vastus,lbl_a,lbl_b,lbl_c
    aken=Tk()
    aken.geometry("650x260")
    aken.resizable(False,False)
    aken.title("Ruutvõrrand")
    f1=Frame(aken,width=650,height=260)
    f1.pack()

    lbl=Label(f1,text="Ruutvõrrandite lahendus",font="Calibri 26",fg="green",bg="lightblue")
    lbl.grid(row=0, column=0, columnspan=8)

    lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
    lbl_vastus.grid(row=2, column=0, columnspan=8)

    lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_a.grid(row=1,column=0)
    lbl_a.bind("<KeyRelease>" ,entryColor)

    x2=Label(f1,text="x^2+",font="Calibri 26",fg="green",padx=10)
    x2.grid(row=1,column=1)

    lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_b.grid(row=1,column=2)
    lbl_b.bind("<KeyRelease>" ,entryColor)

    x=Label(f1,text="x+",font="Calibri 26",fg="green",padx=10)
    x.grid(row=1,column=3)

    lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
    lbl_c.grid(row=1,column=4)
    lbl_c.bind("<KeyRelease>" ,entryColor)

    y=Label(f1,text="=0",font="Calibri 26",fg="green",padx=10)
    y.grid(row=1,column=5)

    btn_lahenda=Button(f1,text="Lahenda",font="Calibri 26",fg="green",command=Solve)
    btn_lahenda.grid(row=1,column=6)

    btn_graafik=Button(f1,text="Graafik",font="Calibri 26",fg="green",command=Graafik)
    btn_graafik.grid(row=1,column=7)
    
    aken.mainloop()

Aken_grid()