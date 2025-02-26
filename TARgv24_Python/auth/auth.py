from tkinter import *
from string import *
from time import sleep
from os import path, remove
from tkinter import simpledialog as sd
from tkinter import filedialog
import smtplib,ssl,imghdr

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


from email.message import EmailMessage
def saada_kiri():
    kellele=emailentry.get()
    kiri=kirientry.get
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="evgeny.tailov@gmail.com"
    password="xjjt vspa vtnp xcgy"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="hea sõnad" #from Entry
    msg['From']="Evgeny"
    msg['To']=kellele
    with open(file,'rb') as fpilt:
        pilt=fpilt.read()
    msg.add.attachment(pilt,maintype='image',subtype=imghdr.what(None.pilt))   
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        print("Informatsioon","Kiri oli saadetud")
    except Exception as e:
        print("Tekkis viga!",e)
    finally:
        server.quit()




def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    l_lisatud.configure(text=file)
    return file

aken=Tk()
aken.geometry("700x550")
aken.title("E-kirja saatmine")
aken.resizable(False,False)
email=Label(text="EMAIL:",font="Calibri 26",fg="white",bg="green",width=10)
email.grid(row=0,column=0)
teema=Label(text="TEEMA:",font="Calibri 26",fg="white",bg="green",width=10)
teema.grid(row=1,column=0)
lisa=Label(text="LISA:",font="Calibri 26",fg="white",bg="green",width=10)
lisa.grid(row=2,column=0)
kiri=Label(text="KIRI:",font="Calibri 26",fg="white",bg="green",width=10)
kiri.grid(row=3,column=0,pady=150)

emailentry=Entry(font="Calibri 26",fg="white",bg="green",width=25)
emailentry.grid(row=0,column=1,padx=50)
teemaentry=Entry(font="Calibri 26",fg="white",bg="green",width=25)
teemaentry.grid(row=1,column=1,padx=50)
kirientry=Text(font="Calibri 26",fg="white",bg="green",width=25,height=6)
kirientry.grid(row=3,column=1,padx=50)

lisapilt=Button(text="LISA PILT",font="Calibri 26",fg="white",bg="green",width=8,command=vali_pilt)
lisapilt.place(x=270,y=470)
saada=Button(text="SAADA",font="Calibri 26",fg="white",bg="green",width=8)
saada.place(x=450,y=470)



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