from logging import config
from tkinter import *
from string import *
from time import sleep
from os import path, remove
from tkinter import simpledialog as sd
from tkinter import filedialog
import smtplib,ssl,imghdr
from tkinter import messagebox
from email.message import EmailMessage
from tkinter import ttk

def send_email(mail):
    # Siin võiks olla kood, mis saadab e-kirja
    print(f"E-kiri saadetud aadressile: {mail}")

def registreerimine(kasutajad:list,paroolid:list)->any:
    """Kirjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list
    """
    root = tk.Tk()
    root.withdraw()
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    mail=sd.askstring("Kirjuta oma e-posti!","Kuhu saada kirja?")
    send_email(mail)
    return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemast!" kui kasutaja on olemas nimekirjas
        Nimi on järjendis kasutajad
        Salasõna on paroolide järjendis
        Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")              
        if nimi in kasutajad:            
            while True:
                parool=input("Sisesta salasõna: ")
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                        print(f"Tere tulemast! {nimi}")
                        break                   
                except:
                    print("Vale nimi või salasõna!")
                    if p==5: 
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajat pole")
def nimi_või_parooli_muutmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Salvestame tekst failisse
    """
    #n=int(input("Mitu: "))
    #for i in range(n):
    #    järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,'a')
    text=input("Sisesta tekst:")
    f.write(text+"\n")
    f.close()
def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - разделитель
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
    
        #k,v=line.strip().split(":")
        #kus_vas[k]=v
        
    fail.close()
    return kus,vas #,kus_vas


kasutajad = []
paroolid = []
# registreerimine(kasutajad,paroolid)

# autoriseerimine(kasutajad,paroolid)

# kirjuta_failisse(kasutajad)








####################################################################

# import smtplib,ssl
# from email.message import EmailMessage
# def saada_kiri(nimi:str, parool:str):
#     kellele=input("Kellele: ")
#     kiri=""
#     smtp_server="smtp.gmail.com"
#     port=587
#     sender_email="evgeny.tailov@gmail.com"
#     password="xjjt vspa vtnp xcgy"
#     context=ssl.create_default_context()
#     msg=EmailMessage()
#     msg.set_content(kiri)
#     msg['Subject']="hea sõnad" #from Entry
#     msg['From']="Evgeny"
#     msg['To']=kellele
#     try:
#         server=smtplib.SMTP(smtp_server,port)
#         server.starttls(context=context)
#         server.login(sender_email,password)
#         server.send_message(msg)
#         print("Informatsioon","Kiri oli saadetud")
#     except Exception as e:
#         print("Tekkis viga!",e)
#     finally:
#         server.quit()


# saada_kiri("Evgeny", 123)

def saada_kiri():
    kellele = emailentry.get().strip().split(",") 
    kiri=kirientry.get("1.0", END).strip()
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="evgeny.tailov@gmail.com"
    password="rwvx hfbo eqbo puyn"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']=teemaentry.get()
    msg['From']="Evgeny"
    msg['To']=kellele

    if not file:
        messagebox.showerror("Tekkis viga!", "Palun vali pilt enne kirja saatmist!")
        return

    try:
        with open(file[0], 'rb') as fpilt:
            pilt = fpilt.read()
        msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Pildi lisamine ebaõnnestus: {e}")
        return
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Kirja saatmine ebaõnnestus: {e}")
    finally:
        server.quit()

file = None

def show_preview():
    kellele = emailentry.get().strip().split(",")
    teema = teemaentry.get()
    kiri = kirientry.get("1.0", END).strip()
    preview_message = f"Email: {', '.join(kellele)}\n\nTeema: {''.join(teema)}\n\nKiri: {''.join(kiri)}"
    messagebox.showinfo("Eelvaade", preview_message)

def lisa_allkiri():
    kirientry.insert(END, "\n\n" + "Parimate soovidega,\nEvgeny Tailov")

def vali_pilt():
    global file
    file = filedialog.askopenfilenames()
    if file:
        lisa_text.configure(text="\n".join(file))
    return file

def puhastamine():
    global file
    emailentry.delete(0, END)
    teemaentry.delete(0, END) 
    kirientry.delete("1.0", END) 
    file = None
    lisa_text.configure(text="...")

aken=Tk()
aken.geometry("900x550")
aken.title("E-kirja saatmine")
aken.resizable(False,False)
email=Label(text="EMAIL:",font="Calibri 26",fg="white",bg="green",width=10)
email.grid(row=0,column=0)
teema=Label(text="TEEMA:",font="Calibri 26",fg="white",bg="green",width=10)
teema.grid(row=1,column=0)
lisa=Label(text="LISA:",font="Calibri 26",fg="white",bg="green",width=10)
lisa.grid(row=2,column=0)
lisa_text = Label(aken, text="...", font=("Times New Roman", 12), padx=38)
lisa_text.grid(row=2, column=1, padx=40)
kiri=Label(text="KIRI:",font="Calibri 26",fg="white",bg="green",width=10)
kiri.grid(row=3,column=0,pady=150)

emailentry=Entry(font="Calibri 26",fg="white",bg="green",width=25)
emailentry.grid(row=0,column=1,padx=50)
teemaentry=Entry(font="Calibri 26",fg="white",bg="green",width=25)
teemaentry.grid(row=1,column=1,padx=50)
kirientry=Text(font="Calibri 26",fg="white",bg="green",width=25,height=6)
kirientry.grid(row=3,column=1,padx=50)

lisapilt=Button(text="LISA PILT",font="Calibri 26",fg="white",bg="green",width=8, command=vali_pilt)
lisapilt.place(x=370,y=470)
saada=Button(text="SAADA",font="Calibri 26",fg="white",bg="green",width=8, command=saada_kiri)
saada.place(x=550,y=470)
Button(text="PUHASTA", font=("Calibri", 26), fg="white",bg="red", width=8, command=puhastamine).place(x=725, y=470)
eelvaade=Button(text="EELVAADE",font="Calibri 26",fg="white",bg="green",width=8, command=show_preview)
eelvaade.place(x=200,y=470)
allkiri=Button(text="ALLKIRI",font="Calibri 26",fg="white",bg="green",width=8, command=lisa_allkiri)
allkiri.place(x=25,y=470)



aken.mainloop()






# if vastus==1:
#     print("Registreerimine")
#     kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
# elif vastus==2:
#     print("Autoriseerimine")
#     autoriseerimine(kasutajanimed,salasõnad)
# elif vastus==3:
#     print("Nime või parooli muutmine")
#     vastus=input("Kas muudame nime, parooli või mõlemad?")
#     if vastus=="nimi":
#         kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
#     elif vastus=="parool":
#         salasõnad=nimi_või_parooli_muutmine(salasõnad)
#     elif vastus=="mõlemad":
#         print("Nimi muutmine: ")
#         kasutajanimed=nimi_või_parooli_muutmine(kasutajanimed)
#         print("Parooli muutmine: ")
#         salasõnad=nimi_või_parooli_muutmine(salasõnad)
#     elif vastus==4:
#         print()