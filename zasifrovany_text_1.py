volba = input("Zasifrovat (s) alebo desifrovat (d)? ")
kluc = input("Zadaj kluc: ")

if volba == "s":
    subor_vstup = open("vstupny_text.txt", "r")
    subor_vystup = open("zasifrovany_text.txt", "w")
else:
    subor_vstup = open("zasifrovany_text_1.txt", "r")
    subor_vystup = open("desifrovany_text.txt", "w")
    
for vstup in subor_vstup:
    vstup = vstup.rstrip("\n")   
    novy_kluc = kluc * (len(vstup) // len(kluc)) + kluc[:len(vstup) % len(kluc)]
    vystup = ""
    for i in range(len(vstup)):
        if 97 <= ord(vstup[i]) and ord(vstup[i]) <= 122:
            posun = ord(novy_kluc[i]) - 96
            if volba == "d":
                posun = -posun
            vystup += chr((ord(vstup[i]) - 97 + posun) % 26 + 97)
        else:
            vystup += vstup[i]
    subor_vystup.write(vystup + "\n")

subor_vstup.close()
subor_vystup.close()