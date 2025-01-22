from random import *

def summa3(arv1:int,arv2:int,arv3:int)->int:
    """Tagastab kolme täisarvu summa

    param int arv1: Esimene number
    param int arv2: Teine number
    param int arv3: Kolmas number
    :rtype: int

    """
    summa=arv1+arv2+arv3
    return summa



def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator.
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param str t: aritmeetiline tehing
    :rtype: var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"

    return vastus

def is_year_leap(y:int)->bool:
    """
    Liigaaasta leidmine
    Tagastab True, kui liigaaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus
    """

    if y%4==0:
         vastus=True
    else:
         vastus=False
    return vastus

def square(a:float)->any:
    S=a**2
    P=4*a
    d=(2)**(1/2)*a
    return S,P,d

def square_text(a:float)->str:
    S=a**2
    P=4*a
    d=(2)**(1/2)

    return "Pindala\n"+str(S)+",Ümbermõõt\n"+str(P)+",Läbimõõt\n"+str(d)





def season(n:int)->str:
    talv = [12,1,2]
    kevad = [3,4,5]
    suvi = [6,7,8]
    sügis = [9,10,11]

    if n in talv:
        vastus = "talv"
    elif n in kevad:
        vastus = "kevad"
    elif n in suvi:
        vastus = "suvi"
    elif n in sügis:
        vastus = "sügis"
    else:
        vastus = "ei ole kuunumber"

    return vastus



def bank(a:float,years:int)->float:
    for i in range(years):
        a*=1.1
    return a



def is_prime(a=randint(0,1000))->bool:
    print(a)
    v=True
    for i in range(2,a):
        if a%i==0:
            v=False
    return v



def date(päev:int,kuu:int,aasta:int)->bool:
    if päev in range(1,31) and kuu in [1,3,5,7,8,10,12]:
        v=True
    elif päev in range(1,29) and kuu==2 and is_year_leap(aasta): # veel tingimus!
        v=True
    elif päev in range(1,30) and kuu in [2,4,6,9,11]:
        v=True
    else:
        v=False
    return v