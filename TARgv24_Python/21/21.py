from tkinter import *
from PIL import Image, ImageTk

def onegame():
    alusta.place_forget()
    vyta=Button(text="Võta kaart",font="Calibri 26",fg="white",bg="green")
    vyta.place(x=300,y=20)
    peatu=Button(text="Peatu",font="Calibri 26",fg="white",bg="green")
    peatu.place(x=500,y=20)

game=Tk()
game.geometry("900x550")
game.title("21")
game.resizable(False,False)
     
original_image = Image.open(r"TARgv24_Python/21/poker.png")
resized_image = original_image.resize((900, 550))
bgimage = ImageTk.PhotoImage(resized_image)

bg=Label(game,image=bgimage)
bg.place(x=0,y=0)

alusta=Button(text="Alusta mängu",font="Calibri 26",fg="white",bg="green",command=onegame)
alusta.place(x=350,y=220)

game.mainloop()