from tkinter import *
from PIL import Image, ImageTk
import random
import os

# tulemuste salvestamine
tulemused = "TARgv24_Python/21/tulemused.txt"
if not os.path.exists(tulemused):
    with open(tulemused, "w") as file:
        file.write("Mängija - Tulemus\n")

# kaardi levitamine
def vyta():
    global player_score, player_cards, kordus
    card = random.randint(2, 11)

    # kui tuleb 11, kontrollime, kas see toob kaasa löögi
    if card == 11 and player_score + 11 > 21:
        card = 1  # kui 11 viib löögini, keera äss 1-ks

    player_cards.append(card)
    player_score += card
    label_score.config(text=f"Sinu tulemus: {player_score}")
    if player_score > 21:
        lopeta("Kaotus! Ületasid 21")
        kordus = Button(game, text=f"Veel üks kord", font="Centaur 26", fg="white", bg="green", command=veel_yks)
        kordus.place(x=70, y=20)


# mängu lõpetamine
def lopeta(result):
    if result == "Võit!":
        label_result.config(fg="green")
    elif result == "Kaotus!":
        label_result.config(fg="red")
    elif result == "Viik!":
        label_result.config(fg="yellow")
    else:
        label_result.config(fg="black")
    label_result.config(text=result)
    label_result.place(x=330, y=250)
    vyta.config(state=DISABLED)
    peatu.config(state=DISABLED)
    tulemuste_salvestamine(result)

# mängu & arvuti tulemuse lõpetamine
def stopp():
    global computer_score, player_score, kordus
    while computer_score < 17:
        computer_score += random.randint(2, 11)
    label_computer_score.config(text=f"Arvuti tulemus: {computer_score}")
    if computer_score > 21 or player_score > computer_score:
        lopeta("Võit!")
    elif player_score > 21 or player_score < computer_score:
        lopeta("Kaotus!")
    else:
        lopeta("Viik!")
    kordus = Button(game, text=f"Veel üks kord", font="Centaur 26", fg="white", bg="green", command=veel_yks)
    kordus.place(x=70, y=20)

def veel_yks():
    global player_score, computer_score, player_cards, kordus
    global vyta, peatu, label_score, label_computer_score, label_result

    player_score = 0
    computer_score = 0
    player_cards = []

    label_result.place_forget()
    kordus.place_forget()
    
    label_score.config(text=f"Sinu tulemus: {player_score}")
    label_computer_score.config(text="Arvuti tulemus: ?")
    
    vyta.config(state=NORMAL)
    peatu.config(state=NORMAL)

# tulemuste salvestamine failis
def tulemuste_salvestamine(result):
    player = player_name.get().strip()
    if not player or player == "Sisesta oma nimi":
        player = "Mängija"
    with open(tulemused, "a") as file:
        file.write(f"{player} - {result} (Tulemus: {player_score})\n")

# mängu alustamine
def alusta_mäng():
    global vyta, peatu, label_score, label_computer_score, label_result
    global player_score, computer_score, player_cards
    player = player_name.get().strip()
    if not player or player == "Sisesta oma nimi":
        player_name.delete(0, END)
        player_name.insert(0, "Mängija")
    alusta.place_forget()
    player_name.place_forget()  # nimi peidamine
    
    player_score = sum(random.sample(range(2, 12), 2))  # 2 rand kaardid
    player_cards = []
    computer_score = random.randint(2, 11)
    
    # labels
    label_score = Label(game, text=f"Sinu tulemus: {player_score}", font="Centaur 26", fg="white", bg="green")
    label_score.place(x=330, y=150)
    
    label_computer_score = Label(game, text="Arvuti tulemus: ?", font="Centaur 26", fg="white", bg="green")
    label_computer_score.place(x=330, y=200)
    
    label_result = Label(game, text="", font="Centaur 26", fg="white", bg="white")
    label_result.place_forget()
    
    vyta = Button(game, text="Võta kaart", font="Centaur 26", fg="white", bg="green", command=vyta)
    vyta.place(x=300, y=20)
    
    peatu = Button(game, text="Peatu", font="Centaur 26", fg="white", bg="green", command=stopp)
    peatu.place(x=500, y=20)

game = Tk()
game.geometry("900x550")
game.title("21")
game.resizable(False, False)

original_image = Image.open("TARgv24_Python/21/poker.png")
resized_image = original_image.resize((900, 550))
bgimage = ImageTk.PhotoImage(resized_image)

bg = Label(game, image=bgimage)
bg.place(x=0, y=0)

def fookus_jah(event):
    if player_name.get() == "Sisesta oma nimi":
        player_name.delete(0, END)  # koristab väli

def fookus_ei(event):
    if player_name.get() == "":
        player_name.insert(0, "Sisesta oma nimi")  # paneb tekst tagasi

player_name = Entry(game, font="Centaur 20", justify="center")
player_name.place(x=315, y=150)
player_name.insert(0, "Sisesta oma nimi")
player_name.bind("<FocusIn>", fookus_jah)
player_name.bind("<FocusOut>", fookus_ei)

alusta = Button(game, text="Alusta mängu", font="Centaur 26", fg="white", bg="green", command=alusta_mäng)
alusta.place(x=350, y=220)

game.mainloop()