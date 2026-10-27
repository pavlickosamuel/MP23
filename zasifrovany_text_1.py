verzia = input("Zašifrovať (s) alebo dešifrovať (d)? ")
kluc = input("Kľúč: ")

if verzia == "s":
    subor_vstup = open("vstupny_text.txt", "r")
    subor_vystup = open("zasifrovany_text.txt", "w")
else:
    subor_vstup = open("zasifrovany_text_1.txt", "r")
    subor_vystup = open("desifrovany_text.txt", "w")


def siforavanie():
    for aa in range(len(vstup)):
        if "a" <= vstup[aa] <= "z":
            ac = ord(vstup[aa])-97
            zmena = chr((ac + posun[aa]) % 26 + 97)
            vystup.append(zmena)
        else:
            vystup.append(vstup[aa])

def desifrovanie():
    for aa in range(len(vstup)):
        if "a" <= vstup[aa] <= "z":
            ac = ord(vstup[aa])-97
            zmena = chr((ac - posun[aa]) % 26 + 97)
            vystup.append(zmena)
        else:
            vystup.append(vstup[aa])


for vstup in subor_vstup:
    vstup = vstup.rstrip("\n")
    prilozeny_kluc = []
    posun = []
    vystup = []

    pocet = len(vstup)//len(kluc)
    zvysok = len(vstup)%len(kluc)

    for i in range(pocet):
        prilozeny_kluc.append(kluc)
    prilozeny_kluc.append(kluc[:zvysok])
    prilozeny_kluc = "".join(prilozeny_kluc)

    for a in range(len(vstup)):
        if "a" <= vstup[a] <= "z":
            posun.append(ord(prilozeny_kluc[a])-96)
        else:
            posun.append(0)

    if verzia == "d":
        desifrovanie()
    elif verzia == "s":
        siforavanie()

    subor_vystup.write("".join(vystup) + "\n")

subor_vstup.close()
subor_vystup.close()

