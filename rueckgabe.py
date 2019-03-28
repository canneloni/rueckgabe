import csv

# Die Bestellnummer des Kunden
bestellNummer = input('Bitte gib deine Bestellnummer ein: ')


# gruende = {'1. Falsches Produkt bestellt.': 1, '2. Falsche Größe bestellt.' : 2, '3. Es wurde ein Produkt zuviel geliefert.' :3, '4. Das Produkt gefällt mir nicht.' : 4, '5. Das Produkt ist defekt angekommen.': 5 }
gruende = {1: '1. Falsches Produkt bestellt.',\
           2: '2. Falsche Größe bestellt.',\
           3: '3. Es wurde ein Produkt zuviel geliefert.',\
           4: '4. Das Produkt gefällt mir nicht.',\
           5: '5. Das Produkt ist defekt angekommen.'}

# Ausgabe der Auswahlmöglichkeiten
print('Es stehen folgende Rückgabegründe zur Auswahl:')
for x in gruende:
    print (gruende[x])

def user_input():
    while True:
        grund_auswahl = input('Bitte gib deinen Rückgabegrund ein: ')
        if grund_auswahl.isdigit():
            if  int(grund_auswahl) <=5 and int(grund_auswahl)>=1:
                print('Ist dein Rückgabegrund: \n'+ gruende[int(grund_auswahl)])
                sicher=input('y=Ja, n=Nein \n')
                if sicher=='y':
                    print('Deine Eingabe wurde gespeichert')
                    return grund_auswahl
                    break
                elif sicher=='n':
                    print('Bitte gib erneut deinen Rückgabegrund ein: ')
                else:
                    print('Bitte gib y für "Ja" und n für "nein" ein: \n')
            else :
                print('Bitte gib eine Zahl zwischen 1 und 5 als Rückgabegrund ein.')
        else :
            print('Du hast keine Zahl von 1-5 eingegeben')
            user_input()
rueckgabeGrund = user_input()

print('Dies ist ein Test um zu gucken, ob die Ausgabe richtig gespeichert wird:')
print(gruende[int(rueckgabeGrund)])

speichern = open('test.txt', 'a')
speichern.write(str(rueckgabeGrund))

# Dies ist ein kleiner Test um zu gucken wie Einfach ein Update bei GIT ist.

# Hier noch ein kleiner kommentar um eine Änderung zu bewirken

