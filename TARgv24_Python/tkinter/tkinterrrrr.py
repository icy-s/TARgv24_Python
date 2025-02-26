from tkinter import *
kvadrat = Tk()
kvadrat.geometry("1000x500")
tablichka = Label(kvadrat,text="решай",font=("Bernadette",50),bg='green')
tablichka.place(x=250, width=500, height=100)
vvod1 = Entry(kvadrat,font=50,bg='green')
vvod1.place(x=50,y=180, width=100,height=100)
uravnenie = Label(kvadrat,text="x**2+",font=("Bernadette",50),bg='green')
uravnenie.place(x=200,y=195)
vvod2 = Entry(kvadrat,font=50, bg='green')
vvod2.place(x=400,y=180, width=100,height=100)






kvadrat.mainloop()