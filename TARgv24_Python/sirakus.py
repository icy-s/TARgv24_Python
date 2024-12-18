print("*** MÄNG NUMBRIDEGA ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisesta täisarv => ")))) #не было двух скобок
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga on mõttetu töö")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Loendame, mitu on paaris ja mitu paaritu arvu")
    print()
    c=b=a # =
    paaris = 0 # =
    paaritu = 0 # =
    while b > 0: # :
            if b % 2 == 0: # ==
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10 # сдвинуто дальше было
    print(f"Paaris arvude kogus: {paaris}") #неправильно закрыт комментарий
    print(f"Paaritu on: {paaritu}") #неправильно закрыт комментарий
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Ümberpöörame* sisestatud arv")
    print()
    b=0
    while a > 0: # :
        number = a % 10
        a = a // 10 
        b = b * 10
        b += number # сдвинуто
    print("*Ümberpööratud arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Tõestame teoreem") #лишняя скобка в начале
    print()
    # if c % 2 == 0: # ==
    #     print(f"{c} - paaris arv. Jagame 2.") #{c}
    # else:
    #     print(f"{c} - paaritu arv. Korrutame 3, liidame 1 ja jagame 2.") #{c}
    while c != 1:
        if c % 2 == 0: # == 
            print('{:>4}'.format(round(c))," - Paaris arv, Jagame 2.")
            c == c / 2
        else:
            print('{:>4}'.format(round(c))," - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
            c == (3*c + 1) / 2
    print()
    print("Teoreem on tõestatud")