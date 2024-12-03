import math  #import math

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Palun sisesta positiivne arv.")
        except ValueError:
            print("Viga: Palun sisesta kehtiv arv.")

print("Ruudu karakteristikud")
a=get_positive_float('Sisesta ruudu külje pikkus => ') #ei olnud float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) # teine " printis oli ''
di=a*math.sqrt(2) #sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #lisa ) lõpuks
b=get_positive_float("Sisesta ristküliku 1. külje pikkus => ") #float
c=get_positive_float("Sisesta ristküliku 2. külje pikkus => ") #float
S=b*c
print('Ristküliku pindala', S) #ei olnud lisatud esimene '
P=2*(b+c) #ei olnud *
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2) # **
print("Ristküliku diagonaal", round(di, 2)) #ei olnud lisatud teine ) ja round 2
print()
print("Ringi karakteristikud")
r=get_positive_float('Sisesta ringi raadiusi pikkus => ') #oli lisatud vale sulged ja float
d=2*r #ei olnud * sümbool
print("Ringi läbimõõt", d) #ei olnud ,
S=math.pi*r**2 #ei olnud math. ja eemaldasin () ja panin lisa *
print("Ringi pindala", round(S, 2)) #round 2
C=2*math.pi*r #ei olnud *math. ja eemaldasin ()
print("Ringjoone pikkus", round(C, 2)) #lõpus panin lisa ) ja round 2