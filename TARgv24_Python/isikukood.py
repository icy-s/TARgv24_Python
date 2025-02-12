ikoodid = []
arvud = []

def kontrollnro(kood):
    kaalud_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaalud_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    summa = sum(int(kood[i]) * kaalud_1[i] for i in range(10))
    jaak = summa % 11
    if jaak != 10:
        return jaak
    summa = sum(int(kood[i]) * kaalud_2[i] for i in range(10))
    jaak = summa % 11
    return 0 if jaak == 10 else jaak

def kontrolli_isikukood(kood):
    if len(kood) != 11:
        print("Isikukood peab olema täpselt 11 numbrit pikk")
        return False
    
    if kood[0] not in "123456":
        print("Isikukoodi esimene number peab olema 1, 2, 3, 4, 5 või 6")
        return False
    
    synniosa = kood[1:7]
    if not synniosa.isdigit():
        print("Sünnikuupäev isikukoodis peab sisaldama ainult numbreid")
        return False
    
    päev = int(synniosa[4:6])
    kuu = int(synniosa[2:4])
    aasta = int(synniosa[0:2])
    
    # täisaasta arvutamine vastavalt esimesele numbrile
    sajand = (int(kood[0]) - 1) // 2
    aasta += 1800 + sajand * 100
    
    try:
        from datetime import date
        synnikuupaev = date(aasta, kuu, päev)
        synnikuupaev_str = synnikuupaev.strftime("%d.%m.%Y")
    except ValueError:
        print("Isikukoodis olev sünnikuupäev on vale")
        return False
    
    kontrollnr = kontrollnro(kood)
    if int(kood[-1]) != kontrollnr:
        print("Kontrollnumber ei klapi")
        return False
    
    sugu = "naine" if kood[0] in "246" else "mees"
    
    haiglakood = int(kood[7:10])
    haigla = ""
    if 1 <= haiglakood <= 10:
        haigla = "Kuressaare Haigla"
    elif 11 <= haiglakood <= 19:
        haigla = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= haiglakood <= 220:
        haigla = "Ida-Tallinna Keskhaigla (või Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla)"
    elif 221 <= haiglakood <= 270:
        haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= haiglakood <= 370:
        haigla = "Maarjamõisa Kliinikum (Tartu) või Jõgeva Haigla"
    elif 371 <= haiglakood <= 420:
        haigla = "Narva Haigla"
    elif 421 <= haiglakood <= 470:
        haigla = "Pärnu Haigla"
    elif 471 <= haiglakood <= 490:
        haigla = "Pelgulinna Sünnitusmaja (Tallinn) või Haapsalu haigla"
    elif 491 <= haiglakood <= 520:
        haigla = "Järvamaa Haigla (Paide)"
    elif 521 <= haiglakood <= 570:
        haigla = "Rakvere või Tapa haigla"
    elif 571 <= haiglakood <= 600:
        haigla = "Valga Haigla"
    elif 601 <= haiglakood <= 650:
        haigla = "Viljandi Haigla"
    elif 651 <= haiglakood <= 700:
        haigla = "Lõuna-Eesti Haigla (Võru) või Põlva Haigla"
    else:
        print("Tundmatu haigla kood")
        return False
    
    ikoodid.append({"kood": kood, "sugu": sugu, "synnikuupaev": synnikuupaev_str, "haigla": haigla})
    print(f"See on {sugu}, tema sünnikuupäev on {synnikuupaev_str} ja sünnikoht on {haigla}")
    return True

def isikukoodide_töötlemine():
    õiged_koodid = 0
    valed_koodid = 0
    while õiged_koodid < 5 and valed_koodid < 5: # tsükli piirang
        kood = input("Sisestage isikukood: ")
        if kontrolli_isikukood(kood):
            õiged_koodid += 1
        else:
            valed_koodid += 1
            arvud.append(kood)
    
    ikoodid.sort(key=lambda x: (x['sugu'] == 'mees', x['synnikuupaev']))
    print("Õiged isikukoodid:")
    for kood in ikoodid:
        print(f"See on {kood['sugu']}, tema sünnikuupäev on {kood['synnikuupaev']} ja sünnikoht on {kood['haigla']}")
    
    arvud.sort()
    print("\nValed isikukoodid:")
    for kood in arvud:
        print(kood)

isikukoodide_töötlemine()