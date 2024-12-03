from datetime import *
from calendar import *
from random import *
from math import *

#ülesanne 1
paevadekogus=monthrange(2024,11)[1] #calendar modulist
print(paevadekogus)

tana=date.today() #nimetus()-funkstioon
tanaf=date.today().strftime("%B %d, %Y")

print(f"Tere! Täna on {tanaf}")
d=tana.day #nimetus - omadus
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

detsP=monthrange(2024,12)[1] #31
novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta lõpuni on {jaak}")
print(f"Kuu lõpuni on {jaak2}")

#ülesanne 2
vastus1=3 + 8 / (4 - 2) * 4
vastus2=3 + 8 / 4 - 2 * 4
vastus3=(3 + 8) / (4 - 2) * 4
vastus4=round((3 + 8) / (4 - 2) * 4)
print(vastus1,"\n",vastus2,"\n",vastus3,"\n",vastus4)

#ülesanne 3
#1 variant
try:
    R=float(input("Sisesta R: "))
    Sk=pi*R**2
    Lk=2*pi*R
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}\n")
except:
    print("On vaja number!")

#2 variant
R=random()*100 #0.0...1.0
print(f"R={R}")
Sk=pi*R**2
Lk=2*pi*R
Skv=(2*R)**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi ümbermõõt on {Lk}\nRuudu pindala on {Skv}\nRuudu ümbermõõt on {Lkv}\n")

#ülesanne 4
d=2.575 # mündi d
maa=6378 #maa radius km
maa*=100000 #maa radium sm + maa=maa*100000
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"On vaja {kogus} mündi.\nMeil on vaja {kogus*2} eur")

#ülesanne 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

#ülesanne 6
sõnad = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.
"""
print(sõnad.upper())

#ülesanne 7
a = float(input("Sisesta ristküliku esimese külje pikkus (a): "))
b = float(input("Sisesta ristküliku teise külje pikkus (b): "))
umbermoot = 2*(a+b)
pindala = a*b
print(f"Ristküliku ümbermõõt on {umbermoot:.2f}")
print(f"Ristküliku pindala on {pindala:.2f}")

#ülesanne 8
kogus = float(input("Sisesta tarbitud liitrid: "))
km = float(input("Sisesta läbitud kilomeetrid: "))
keskmine = (kogus*100)/km
print(f"Sinu keskmine kütusekulu on {keskmine:.1f}L 100 kilomeetri kohta.")

#ülesanne 9
M = float(input("Sisestage minutite arv: "))
kiirus = 29.9
minutid = M/60
distance = (minutid*kiirus)
print(f"Saad sõita {distance:.1f} kilomeetrit {M:.1f} minutiga.")

#ülesanne 10
ms = int(input("Sisestage minutite arv: "))
hours = ms/60
minutes = ms%60 #вычисляет остаток
print(f"{ms} on {hours:.0f}:{minutes}")