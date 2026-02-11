vstup = input("Zadaj text na zasifrovanie: ")
kluc = input("Zadaj kluc: ")
#novy kluc bude rovnaky ako povodny kluc, ale opakovany na celu dlzku vstupu
novy_kluc = kluc * (len(vstup) // len(kluc)) + kluc[:len(vstup) % len(kluc):]
print (len(novy_kluc), len(vstup))
vystup = ""
for i in range(len(vstup)):
    if 97 <= ord(vstup[i]) and ord(vstup[i]) <= 122: 
        posun = ord(novy_kluc[i]) - 96
        vystup += chr((ord(vstup[i]) - 97 + posun) % 26 + 97)
    else:
        vystup += vstup[i]
print(vystup)