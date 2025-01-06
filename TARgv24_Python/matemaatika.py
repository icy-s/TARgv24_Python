import random

print("Tere tulemast matemaatikatesti!")
print("Valige raskusaste:")
print("1. Lihtne")
print("2. Keskmine")
print("3. Raske")

while True:
    try:
        raskusaste = int(input("Sisestage raskusastme number (1-3): "))
        if raskusaste in [1, 2, 3]:
            break
        else:
            print("Palun sisestage number vahemikus 1 kuni 3.")
    except ValueError:
        print("Vale sisend. Proovige uuesti")

küsimuste_arv = int(input("Mitu ülesannet soovite lahendada? "))
õiged_vastused = 0

for _ in range(küsimuste_arv): # _, потому что использовать конкретную переменную в теле цикла не требуется
    if raskusaste == 1:
        arv_vahemik = 10
        tehted = ['+', '-']
    elif raskusaste == 2:
        arv_vahemik = 50
        tehted = ['+', '-', '*', '/']
    else:
        arv_vahemik = 100
        tehted = ['+', '-', '*', '/', '**']

    tehe = random.choice(tehted)
    arv1 = random.randint(1, arv_vahemik)
    arv2 = random.randint(1, arv_vahemik)

    if tehe == '/' and arv2 == 0:
        arv2 = random.randint(1, arv_vahemik)  # чтобы избежать деления на ноль

    if tehe == '/':
        print(f"Lahendage: {arv1} {tehe} {arv2} (ümardage kahe komakohani)")
    else:
        print(f"Lahendage: {arv1} {tehe} {arv2}")

    while True:
        try:
            kasutaja_vastus = float(input("Teie vastus: "))
            break
        except ValueError:
            print("Palun sisestage arvuline väärtus.")

    if tehe == '+':
        oige_vastus = arv1 + arv2
    elif tehe == '-':
        oige_vastus = arv1 - arv2
    elif tehe == '*':
        oige_vastus = arv1 * arv2
    elif tehe == '/':
        oige_vastus = round(arv1 / arv2, 2)
    elif tehe == '**':
        oige_vastus = arv1 ** arv2

    if abs(kasutaja_vastus - oige_vastus) < 0.01:
        print("Õige!")
        õiged_vastused += 1
    else:
        print(f"Vale. Õige vastus: {oige_vastus}")

tulemus = (õiged_vastused / küsimuste_arv) * 100
print(f"\nTeie tulemus: {õiged_vastused} õiged {küsimuste_arv} küsimust ({tulemus:.2f}%)")

if tulemus < 60:
    hinne = 2
elif 60 <= tulemus < 75:
    hinne = 3
elif 75 <= tulemus < 90:
    hinne = 4
else:
    hinne = 5

print(f"Teie hinne: {hinne}")