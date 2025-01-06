vanaisa = "Vanaisa"
vanaema = "Vanaema"
laps = "Laps"
koer = "Koer"
kass = "Kass"
hiir = "Hiir"
tegelased = [vanaisa, vanaema, laps, koer, kass, hiir]
for tegelane in tegelased:
    if tegelane == "Hiir":
        print(f"{tegelane} tuli ja tõmbas repka välja!")
    else:
        print(f"{tegelane} tuli ja aitab repkat tõmmata.")