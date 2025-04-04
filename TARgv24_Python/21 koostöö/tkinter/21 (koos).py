from tkinter import *
from tkinter import messagebox
from turtle import color
from PIL import Image, ImageTk
from numpy import size
import random


root=Tk()
root.geometry("800x500")
root.resizable(False,False)
root.title("21")

c = 0
points = 0

def game():
    global a, b
    global points
    global name
    name = Pname.get()
    
    if name == "":
        nameLabel.configure(text= "Please enter the name!")
        showStartMenu()
    else:
        nameLabel.configure(text= "Who is playing?")
        button1.place_forget()
        nameLabel.place_forget()
        Pname.place_forget()
        History.place_forget()

        a = random.randint(2, 11)
        b = random.randint(2, 11)

        card1.configure(text= str(a))
        card1.place(x=100, y=100)
        card2.configure(text= str(b))
        card2.place(x=500, y=100)

        points = a + b

        summa.configure(text=(f"{a+b}"))
        summa.place(x=350, y=20)
        pause.place(x=200, y=400)
        TakeCard.place(x=500, y=400)
        return a, b, name

   

    

def pauseChoisedef():
    global points
    card1.place_forget()
    card2.place_forget()
    card3.place_forget()
    pause.place_forget()
    TakeCard.place_forget()
    summa.place_forget()


    result.configure(text=(f"You've earned {points} points!"))
    result.place(x=250, y=80)

    save_result(name, points)

    Continue.place(x=340, y = 360)
 

def TakeCardChoisedef():
    global points
    c = random.randint(2, 11)
    card1.place(x=50, y=100)
    card2.place(x=300, y=100)
    card3.configure(text= str(c))
    card3.place(x=550, y=100)
    summa.configure(text=(f"{a+b+c}"))
    summa.place_forget()
    pause.place_forget()
    TakeCard.place_forget()
    
    points = a + b + c
    if points <= 21 :
        result.configure(text=(f"You've earned {points} points!"))
        result.place(x=250, y=20)
    elif points >21:
        result.configure(font=("beer money", 30), text=(f"The result is {points}, which is greater than 21,\n   you lose all your points..."))
        result.place(x=100, y=20)
        points = 0

    save_result(name, points)

    Continue.place(x=340, y = 400)

   
def showStartMenu():
    global name
    global points
    name = Pname.get()
    Pname.delete(0, END)
    points = 0
    Continue.place_forget()
    pause.place_forget()
    TakeCard.place_forget()
    summa.place_forget()
    result.place_forget()
    card1.place_forget()
    card2.place_forget()
    card3.place_forget()
    ReadResultsLabel.place_forget()
    ClearHistory.place_forget()
    Back.place_forget()


    Pname.place(x=240, y=180)
    button1.place(x=340, y = 360)
    History.place(x=140, y = 360)
    
    if name == "":
        nameLabel.place(x=200, y=50)
    else:
        nameLabel.place(x=260, y=50)
    





def save_result(name, points):
    with open(r"C:\Users\xicey\source\repos\icy-s\TARgv24_Python\TARgv24_Python\21 koostöö\results.txt", "r", encoding="utf-8") as f:
        scores = f.read()

    if scores ==  """ В этой history

 мышб повесилась

   🐀""":

        with open(r"C:\Users\xicey\source\repos\icy-s\TARgv24_Python\TARgv24_Python\21 koostöö\results.txt", "w", encoding="utf-8") as f:
            pass

    with open(r"C:\Users\xicey\source\repos\icy-s\TARgv24_Python\TARgv24_Python\21 koostöö\results.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{name}: ({points} points)")

def show_result():
    button1.place_forget()
    nameLabel.place_forget()
    Pname.place_forget()
    History.place_forget()

    with open(r"C:\Users\xicey\source\repos\icy-s\TARgv24_Python\TARgv24_Python\21 koostöö\results.txt", "r", encoding="utf-8") as f:
        scores = f.read()
    ReadResultsLabel.configure(text=scores)
    ReadResultsLabel.place(x=350, y=0)

    Back.place(x=140, y = 360)
    ClearHistory.place(x=90, y = 160)

def clear_history():

    with open(r"C:\Users\xicey\source\repos\icy-s\TARgv24_Python\TARgv24_Python\21 koostöö\results.txt", "w", encoding="utf-8") as f:
        f.write(" В этой history\r\n мышб повесилась\r\n   🐀")
    show_result()
    
    



original_image = Image.open(r"TARgv24_Python/21 koostöö/tkinter/ttt.png")
resized_image = original_image.resize((800, 500))  # Resize to window size
bgimage = ImageTk.PhotoImage(resized_image)

labelBG=Label(root,image=bgimage)
labelBG.place(x=0,y=0)

button1=Button(root,text="Start",font=("beer money", 45), bg="#36051c", command=game) #command = Start
button1.place(x=340, y = 360)
History= Button(root,text="History",font=("beer money", 30), bg="#36051c", command = show_result)
History.place(x=140, y = 360)

cardImage=Image.open(r"TARgv24_Python/21 koostöö/tkinter/images.png")
bgCardImage=ImageTk.PhotoImage(cardImage)


card1=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')
card2=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')
card3=Label(root, image=bgCardImage, text="nr",font=("beer money", 45), compound='center')

result=Label(root, bg='pink', text=" ", font=("beer money", 30))
ReadResultsLabel=Label(root, bg='pink', text="", font=("beer money", 30))

nameLabel=Label(root, bg='pink', text="Who is playing?", font=("beer money", 35))
nameLabel.place(x=260, y=50)
Pname = Entry(root, bg='pink', font=("beer money", 35))
Pname.place(x=240, y=180)

summa=Label(root, bg='pink', text="nr", font=("beer money", 30), width=5)

pause=Button(root,text="Pause",font=("beer money", 30), bg="#36051c", command=pauseChoisedef)
TakeCard=Button(root,text="Take card",font=("beer money", 30), bg="#36051c", command = TakeCardChoisedef)
Continue=Button(root,text="Continue",font=("beer money", 30), bg="#36051c", command = showStartMenu)
Back=Button(root,text="Back",font=("beer money", 30), bg="#36051c", command = showStartMenu)
ClearHistory=Button(root,text="Clear History",font=("beer money", 30), bg="#36051c", command = clear_history)






root.mainloop()
