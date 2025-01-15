# #ül 1

# import string
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="qwrtpsdfghklzxcvbnm"
# märkid=string.punctuation # %&'()*+,-./:;<=>?@[\]^_`{|}~    
# while True:
#     v=k=m=t=0
#     tekst=input("Sisesta mingi tekst: ").lower()
#     if tekst.isdigit():
#         break
#     else:
#         tekst_list=list(tekst)
#         print(tekst_list) # "p", "r"
#         for täht in tekst_list:
#             if täht in vokaali:
#                 v+=1
#             elif täht in konsonanti:
#                 k+=1
#             elif täht in märkid:
#                 m+=1
#             elif täht == " ":
#                 t+=1
#     print("vokaali: ", v)
#     print("konsonanti: ", k)
#     print("märkid: ", m)
#     print("täht: ", t)

# #ül 2
# nimed=[]
# for i in range(5):
#     nimi=input(f"Sisesta {i+1} nimi: ")
#     nimed.append(nimi) # отправляет nimi в список nimed
# print("Enne sorteerimist:")
# print(nimed)
# nimed.sort()
# print("Sorteerimise pärast:")
# print(nimed)
# print(f"Viimasena lisatud nimi on: {nimi}")
# v=input("Kas muudame nimeid?: ").lower()
# if v=="jah":
#     v=input("Nimi või positsioon: N/P").upper()
#     if v=="P":
#         print("Sisesta nime asukoht")
#         v=int(input())
#         uus_nimi=input("Uus nimi: ")
#         nimed[v-1]=uus_nimi
#     else:
#         print("Sisesta nimi")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
#     print(nimed)


# #1 variant dublikatid
# dublta=list(set(nimed))
# print(dublta)

# #2 variant dublikatid
# dublta=[]
# for nimi in nimed:
#     if nimi not in dublta:
#         dublta.append(nimi)
# print(dublta)

# vanused=[]
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: ")) #i+1 показывает какой это по счёту раз
#     vanused.append(vanus) #отправить результат vanus в список vanused
# print(f"Sisestatud vanused: {vanused}")
# print(max(vanused))
# print(min(vanused))
# print(sum(vanused)/len(vanused))

# #ül 3
# väärtused=[]
# read=int(input("Reade kogus: "))
# for i in range(read):
#     arv=int(input("Arv: "))
#     väärtused.append(arv)
# print(väärtused)
# s=input("Sümbol: ")
# for väärtus in väärtused:
#     print(väärtus*s)

#ül 4
indexid=['Tallinn','Narva, Narva-Jõesuu','Kohtla-Järve','Ida-Virumaa, Lääne-Virumaa, Jõgevamaa','Tartu linn','Tartumaa, Põlvamaa, Võrumaa, Valgamaa','Viljandimaa, Järvamaa, Harjumaa, Raplamaa','Pärnumaa','Läänemaa, Hiiumaa, Saaremaa']

while 1:
    try:
        postiindeks=int(input("Sinu postiindeks: "))
        if len(str(postiindeks))==5:
            break
        else:
            print("On vaja 5 sümboleid!")
    except:
        print("...")
print("Postiindeks analüüs: ")
indekslist=list(str(postiindeks)) # "4", "2", "3"
s1=int(indekslist[0]) # 4
print(f"Postiindeks {postiindeks} on {indexid[s1-1]} piirkond") #12345g