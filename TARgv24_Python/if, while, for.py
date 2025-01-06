#ülesanne 1
N = int(input("Sisesta, kui palju arve sisestada: "))
max_arv = None
for i in range(N):
    arv = int(input(f"Sisesta {i+1}. arv: "))
    if max_arv is None or arv > max_arv:
        max_arv = arv
print(f"Maksimaalne sisestatud arv on: {max_arv}")

#ülesanne 2
while True:
    number = int(input("Sisesta täisarv: "))
    if number == 13:
        print(77)
    else:
        print(number)
    break

#ülesanne 3
päeva_kaugus = 10 # км в первый день
kogusumma = 0 # начальное значение
for päev in range(7):
    kogusumma += päeva_kaugus
    päeva_kaugus *= 1.10
print(f"Sportlane jookseb 7 päeva jooksul kokku {kogusumma:.2f} km")

#ülesanne 4
kokku_tk = float(input("Sisesta kokku materjali pikkus (m): "))
kasutatud_tk = 0  # количество использованного материала (вначале)
while True:
    tulevane_pikkus = float(input("Sisesta, kui pika tüki tahad kasutada (m): "))
    if tulevane_pikkus > kokku_tk - kasutatud_tk:
        print("Materjalist ei piisa!")   
        vastus = input("Kas soovite osta viimase tüki? (jah/ei): ").lower()       
        if vastus == "jah":
            print(f"Viimane tükk müüdi")
            break
        else:
            print("Järgmine ostja")
    else:
        kasutatud_tk += tulevane_pikkus
        print(f"Kasutatud materjal: {kasutatud_tk:.2f} m. Jäänud materjal: {kokku_tk - kasutatud_tk:.2f} m.")

#ülesanne 5
while True:
    a = float(input("Sisesta alumise põhja pikkus (a): "))
    b = float(input("Sisesta ülemise põhja pikkus (b): "))
    h = float(input("Sisesta kõrgus (h): "))    
    pindala = (a + b) * h / 2
    print(f"Trapetsi pindala on: {pindala:.2f} ruutmeetrit.")
    jätkata = input("Kas tahate arvutada veel ühe trapetsi pindala? (jah/ei): ").lower()   
    if jätkata != "jah":
        print("Ok")
        break

#ülesanne 6
number = int(input("Sisesta täisarv: "))
if number % 3 == 0:
    print("Sisestatud number jaguneb 3-ga täpselt")
else:
    print("Sisestatud number ei jagune 3-ga täpselt")