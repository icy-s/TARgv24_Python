from random import * # * - kõik funktsioonid, as - funktsioonide ümbernimetus
from math import * #pi kasutamiseks
from statistics import *

#ülesanne 1
print("Tere tulemast!")
nimi = input("Mis on sinu nimi? ").capitalize() #lower(),upper(),
print("Tere tulemast! Tervitan sind ", nimi)
print("Tere tulemast! Tervitan sind "+ nimi)
vanus=int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastat vana")
print(f"Tere tulemast! Tervitan sind {nimi} Sa oled {vanus} aastat vana")

#ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_käib_koolis))

#ülesanne 3
kokku=randint(1,1000)
print(f"kokku on {kokku} kommi")
kommi=int(input("mitu kommi sa tahad? "))
kokku=kokku-kommi
print(f"jääk on {kokku} kommi")

#ülesanne 4
print("Läbimõõdu leidmine ")
#l - ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")

#ülesanne 5
print("Diagonaali leidmine")
n=float(input("Esimene külg: "))
m=float(input("Teine külg: "))
d=sqrt(n**2 + m**2)
print(f"Diagonaal on {round(d,3)}")

#ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg # viga oli siin
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#ülesanne 7
print(mean([randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)]))

#ülesanne 8
print("  @..@")
print(" (----)")
print("( \__/ )")
print('^^ "" ^^')

#ülesanne 9
def perimetr(a:int,b:int,c:int):
    result = a + b + c
    return result

#ülesanne 10
itemprice = 12.90
tip = 1.1
total = itemprice * tip
each = total / 2
print(f"Igaüks peab maksta {each:.2} euro")