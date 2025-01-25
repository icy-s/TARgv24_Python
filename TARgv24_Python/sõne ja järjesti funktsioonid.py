while True:
    print("\nValige funktsioon demonstreerimiseks:")
    print("1. Elemendi lisamine nimekirja (append)")
    print("2. Nimekirjade ühendamine (extend)")
    print("3. Elemendi indeksi leidmine (index)")
    print("4. Elemendi eemaldamine (remove)")
    print("5. Elemendi olemasolu kontrollimine (in)")
    print("6. Esinemiste arvu lugemine (count)")
    print("7. Nimekirja ümberpööramine (reverse)")
    print("8. Nimekirja sorteerimine (sort)")
    print("9. Stringi jagamine (split)")
    print("10. Nimekirja ühendamine stringiks (join)")

    valik = input("Sisestage funktsiooni number: ")

    if valik == "1":
        minu_loend = [1, 2, 3]
        print(f"{minu_loend}")
        minu_loend.append(4)  # elemendi lisamine nimekirja lõppu
        print(f"Nimekiri pärast append: {minu_loend}")
        print("Funktsioon teostab elemendi lisamine nimekirja lõppu")

    elif valik == "2":
        loend1 = [1, 2, 3]
        loend2 = [4, 5, 6]
        print(f"Loend 1: {loend1}")
        print(f"Loend 2: {loend2}")
        loend1.extend(loend2)  # kahe nimekirja ühendamine
        print(f"loend1 pärast extend: {loend1}")
        print("Funktsioon teostab kahe nimekirja ühendamine")

    elif valik == "3":
        minu_loend = [10, 20, 30, 20]
        print(f"{minu_loend}")
        indeks = minu_loend.index(20)  # esimese esinemise indeksi leidmine
        print(f"Esimese 20 esinemise indeks: {indeks}")
        print("Funktsioon teostab esimese esinemise indeksi leidmine (lugemine algab 0-st)")

    elif valik == "4":
        minu_loend = [1, 2, 3, 2]
        print(f"{minu_loend}")
        minu_loend.remove(2)  # esimese esinemise eemaldamine
        print(f"Nimekiri pärast '2' remove: {minu_loend}")
        print("Funktsioon teostab esimese esinemise eemaldamine")

    elif valik == "5":
        minu_loend = ["õun", "banaan", "kirss"]
        print(f"{minu_loend}")
        print("Kas 'õun' on nimekirjas?", "õun" in minu_loend)  # elemendi olemasolu kontrollimine
        print("Kas 'viinamari' on nimekirjas?", "viinamari" in minu_loend)  # elemendi puudumise kontrollimine
        print("Funktsioon teostab elemendi olemasolu või puudumise kontrollimine")

    elif valik == "6":
        minu_loend = [1, 2, 2, 3, 2]
        count = minu_loend.count(2)  # elemendi esinemiste arvu lugemine
        print(f"{minu_loend}")
        print(f"Elemendi '2' esinemiste arv: {count}")
        print("Funktsioon teostab elemendi esinemiste arvu lugemine")

    elif valik == "7":
        minu_loend = [1, 2, 3]
        print(f"Nimekiri enne reverse: {minu_loend}")
        minu_loend.reverse()  # nimekirja ümberpööramine
        print(f"Nimekiri pärast reverse: {minu_loend}")
        print("Funktsioon teostab nimekirja ümberpööramine")

    elif valik == "8":
        minu_loend = [3, 1, 2]
        print(f"Nimekiri enne sort: {minu_loend}")
        minu_loend.sort()  # nimekirja sorteerimine
        print(f"Nimekiri pärast sort: {minu_loend}")
        print("Funktsioon teostab nimekirja sorteerimine")

    elif valik == "9":
        minu_string = "Tere, maailm!"
        sõnad = minu_string.split(", ")  # stringi jagamine alamstringideks
        print(f"Nimekiri enne split: {minu_string}")
        print(f"Nimekiri pärast split: {sõnad}")
        print("Funktsioon teostab stringi jagamine alamstringideks")

    elif valik == "10":
        minu_loend = ["õun", "banaan", "kirss"]
        tulemus = ", ".join(minu_loend)  # nimekirja ühendamine stringiks
        print(f"String enne join: {minu_loend}")
        print(f"String pärast join: {tulemus}")
        print("Funkstioon teostab nimekirja ühendamine stringiks valitud elementidega")

    else:
        print("Vale valik")

    kordus = input("Kas soovite vaadata veel mõnda funktsiooni? (jah/muu sõne väljumiseks): ").lower()
    if kordus != "jah":
        print("Programmist väljutakse")
        break