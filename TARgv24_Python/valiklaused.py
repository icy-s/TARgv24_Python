import math

#ülesanne 1
number = float(input("Sisestage number: "))
if number > 0:
    print("Arv on positiivne")
    if number % 2 == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
elif number < 0:
    print("Arv on negatiivne")
else:
    print("Arv on null")

#ülesanne 2
nurk1 = float(input("Sisestage esimene arv: "))
nurk2 = float(input("Sisestage teine arv: "))
nurk3 = float(input("Sisestage kolmas arv: "))
if nurk1 > 0 and nurk2 > 0 and nurk3 > 0:
    if nurk1 + nurk2 + nurk3 == 180:
        print("Arvud võivad olla kolmnurga nurgad")
        if nurk1 == nurk2 == nurk3:
            print("Kolmnurk on võrdkülgne")
        elif nurk1 == nurk2 or nurk2 == nurk3 or nurk1 == nurk3:
            print("Kolmnurk on võrdhaarne")
        else:
            print("Kolmnurk on isekülgne")
    else:
        print("Arvud ei saa olla kolmnurga nurgad, kuna nende summa ei ole võrdne 180-ga")
else:
    print("Üks või mitu numbrit ei ole positiivsed")

#ülesanne 3
def nädalapäev():
    päevad = {
        1: "esmaspäev",
        2: "teisipäev",
        3: "kolmapäev",
        4: "neljapäev",
        5: "reede",
        6: "laupäev",
        7: "pühapäev"
    }
    vastus = input("Kas soovite dešifreerida nädalapäeva järjekorranumbri? (jah/ei): ").lower() #lower для того, чтобы можно было вводить и большими буквами
    if vastus == "jah":
        try:
            number = int(input("Sisestage arv vahemikus 1 kuni 7: "))
            if 1 <= number <= 7:
                print(f"Seda nädalapäev: {päevad[number]}.")
            else:
                print("Viga: arv peab jääma 1 ja 7 vahele")
        except ValueError:
            print("Viga: numbrit pole sisestatud")
    else:
        print("Toiming tühistati")

nädalapäev() 

#ülesanne 4
def sodiaagimärk(päev, kuu):
    if not (1 <= kuu <= 12):
        return "Viga: kuu peab olema vahemikus 1 kuni 12"
    if not (1 <= päev <= 31):
        return "Viga: päev peab olema vahemikus 1 kuni 31"
    if kuu in {4, 6, 9, 11} and päev > 30:
        return "Viga: antud kuul võib olla maksimaalselt 30 päeva"
    if kuu == 2:
        if päev > 29:
            return "Viga: veebruaris võib olla maksimaalselt 29 päeva"
    if (kuu == 3 and päev >= 21) or (kuu == 4 and päev <= 19):
        return "Jäär"
    elif (kuu == 4 and päev >= 20) or (kuu == 5 and päev <= 20):
        return "Sõnn"
    elif (kuu == 5 and päev >= 21) or (kuu == 6 and päev <= 20):
        return "Kaksikud"
    elif (kuu == 6 and päev >= 21) or (kuu == 7 and päev <= 22):
        return "Vähk"
    elif (kuu == 7 and päev >= 23) or (kuu == 8 and päev <= 22):
        return "Lõvi"
    elif (kuu == 8 and päev >= 23) or (kuu == 9 and päev <= 22):
        return "Neitsi"
    elif (kuu == 9 and päev >= 23) or (kuu == 10 and päev <= 22):
        return "Kaalud"
    elif (kuu == 10 and päev >= 23) or (kuu == 11 and päev <= 21):
        return "Skorpion"
    elif (kuu == 11 and päev >= 22) or (kuu == 12 and päev <= 21):
        return "Ambur"
    elif (kuu == 12 and päev >= 22) or (kuu == 1 and päev <= 19):
        return "Kaljukits"
    elif (kuu == 1 and päev >= 20) or (kuu == 2 and päev <= 18):
        return "Veevalaja"
    elif (kuu == 2 and päev >= 19) or (kuu == 3 and päev <= 20):
        return "Kalad"
    else:
        return "Viga: valed andmed"
def main():
    try:
        päev = int(input("Sisestage sünnipäev (1-31): "))
        kuu = int(input("Sisestage sünnikuu (1-12): "))
        tulemus = sodiaagimärk(päev, kuu)
        print(tulemus)
    except ValueError:
        print("Viga: palun sisestage ainult täisarvud päeva ja kuu jaoks")

main()

#ülesanne 5
def process_input(user_input):
    if user_input.isdigit():
        number = int(user_input)
        tulemus = number // 2
        print(f"Täisarv: {number}, 50% sellest: {tulemus}")
    else:
        try:
            number = float(user_input)
            if number.is_integer():
                result = int(number) // 2
                print(f"Täisarv: {int(number)}, 50% sellest: {result}")
            else:
                result = number * 0.7
                print(f"Murdarv: {number}, 70% sellest: {result}")
        except ValueError:
            print(f"See on tekst: {user_input}")
def main():
    user_input = input("Sisestage arv või tekst: ")
    process_input(user_input)

main()

#ülesanne 6
def lahenda_ruutvõrrand():
    vastus = input("Kas soovite lahendada ruutvõrrandi? (Jah/Ei): ").lower()   
    if vastus == "jah":
        a = float(input("Sisesta a väärtus: "))
        b = float(input("Sisesta b väärtus: "))
        c = float(input("Sisesta c väärtus: "))
        D = b ** 2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"Kaks lahendust: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif D == 0:
            x = -b / (2 * a)
            print(f"Üks lahendus: x = {x:.2f}")
        else:
            print("Lahendusi pole")
    else:
        print("Head aega!")

lahenda_ruutvõrrand()