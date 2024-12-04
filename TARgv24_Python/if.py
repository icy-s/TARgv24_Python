#ülesanne 1
# nimi=input("Mis on sinu nimi? ")
# if nimi.isalpha() and nimi.isupper():
#    if nimi=="JUKU":
#        print("v kino idu")
#        try:
#             vanus=int(input(f"Kui vana sa oled {nimi}?"))
#             if vanus<0:
#                 print("Viga!")
#             elif vanus<=6:
#                 print("Tasuta")
#             elif vanus<15:
#                 print("Lastepilet")
#             elif vanus<65:
#                 print("Täispilet")
#             elif vanus<100:
#                 print("Sooduspilet")
#             else:
#                 print("bro mogila plachet...")
#        except:
#             print("Täisarv oli vaja sisestada")
#    else:
#        print("v kino ne idu")
# else:
#     print("Segatud sõne")

# #ülesanne 2

# #1 variant
# nimi1=input("1. Mis on sinu nimi? ")
# nimi2=input("2. Mis on sinu nimi? ")
# nimed=["Ksenia","Aleksander"]
# if nimi1.isalpha() and nimi2.isalpha():
#     if (nimi1 in nimed) and (nimi2 in nimed):
#         print("Nad on pinginaabrid")
#     else:
#         print("OLed varas")
# else:
#     print("Viga")

# #2 variant
# if (nimi1=="Aleksander" and nimi2=="Ksenia") or (nimi2=="Aleksander" and nimi1=="Ksenia"):
#     print("Nad on pinginaabrid")
# else:
#         print("OLed varas")

# #ülesanne 3
# try:
#     a=float(input("Pikkus: "))
#     b=float(input("Toa laius: "))
#     S=a*b
#     print(f"Põranda pindala on {S} m2")
#     vastus=input("Kas tahad remondi teha?(Jah,1/Ei,0)") #jah/ei JAH/EI Jah/Ei
#     if vastus.upper()=="JAH" or vastus=="1":
#         print("Remont")
#         hind=float(input("Ühe meetri hind: "))
#         summa=hind*S
#         print(f"Remondi kulud: {summa} eur")

#     elif vastus.upper()=="EI" or vastus=="0":
#         print("-")
#     else:
#         print("ne pon")   
# except:
#     print("kus on numbrid???")

#ülesanne 4
# try:
#     highcost=float(input("Sisestage alghind: "))
#     costah=highcost*0.3
#     costahga=highcost-costah
#     if highcost < 700:
#         print ("skidki ne budet")
#     else:
#         print (f"skidka budet, vasha skidka {costah:.1f}, final summa - {costahga:.1f}")
# except:
#     print("wrong value")

#ülesanne 5
# try:
#     temp=float(input("Sisestage temperatuur: "))
#     if temp >= 18:
#         print ("on 18 kraadi või üle")
#     if temp < 18:
#         print ("ei üle 18 kraadi")
# except:
#     print("wrong value +_+")

#ülesanne 6
# try:
#     pikkus=float(input("Sisestage pikkus: "))
#     if pikkus<70:
#                 print("Viga!")
#     elif pikkus<160:
#                 print("Lühike")
#     elif pikkus<170:
#                 print("Keskmine")
#     elif pikkus<200:
#                 print("Suur")
#     else:
#         print("vah kakoi da")
# except:
#     print("wrong value -_-")

#ülesanne 7
try:
    pikkus=float(input("Sisestage pikkus: "))
    if pikkus<70:
                print("Viga!")
    elif pikkus<160:
                print("Lühike")
    elif pikkus<170:
                print("Keskmine")
    elif pikkus<200:
                print("Suur")
    else:
        print("vah kakoi da")
except:
    print("wrong value -_-")

try:
    sugu=input("Sisestage sugu: 'M' mehele ja 'N' nainele: ")
    if sugu == 'N':
        print("женщина")
    elif sugu == 'M':
        print("мужчина")
    else:
        print("Ainult 'M' või 'N'!")
except:
    print("viga")



    #ДОДЕЛАТЬ 7 ЗАДАНИЕ
