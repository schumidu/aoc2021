from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

class Zahl:
    def __init__(self, zahl):
        self.zahl = zahl
        self.gezogen = False

    def __repr__(self) -> str:
        erg = str(self.zahl)
        if self.gezogen:
            erg += ' x'
        else:
            erg += ' o'
        return erg
    
    def Setgezogen(self):
        self.gezogen = True

    def isGezogen(self):
        return self.gezogen

class Bingofeld:
    def __init__(self) -> None:
        self.feld = []
        self.deleted = False

    def __repr__(self) -> str:
        erg = ''
        for row in self.feld:
            erg += str(row)
            erg += '\n'
        return erg
    
    def addRow(self, row):
        row = row.split()
        newRow = []
        for i in row:
            newRow.append(Zahl(int(i)))
        self.feld.append(newRow)
    
    def addZahl(self, Gzahl):
        for row in self.feld:
            for zahl in row:
                if zahl.zahl == Gzahl:
                    zahl.Setgezogen()
    
    def isFertig(self):
        counter = 0
        #Reihen prüfen
        for i in self.feld:
            counter = 0
            for y in i:
                if y.isGezogen():
                    counter += 1
            if counter == len(i):
                return True

        #Spalten prüfen
        for i in range(len(self.feld[0])):
            counter = 0
            for row in self.feld:
                if row[i].isGezogen():
                    counter +=1
            if counter == len(self.feld[0]):
                return True

        return False
    
    def getSumme(self) -> int:
        summe = 0
        for row in self.feld:
            for i in row:
                if not i.isGezogen():
                    summe += i.zahl
        return summe


if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    liste = readListFromFile('daten.txt')
    zahlen = liste.pop(0).split(',')
    bingozahlen = []
    for zahl in zahlen:
        bingozahlen.append(int(zahl))
    liste.pop(0) ## erste Leerzeile noch wegwerfen

    felder = []
    bingoFeld = Bingofeld()
    for zeile in liste:
        if zeile == '':
            felder.append(bingoFeld)
            bingoFeld = Bingofeld()
        else:
            bingoFeld.addRow(zeile)
    felder.append(bingoFeld) #letzes Feld auch noch anhängen
    ergfeld = None
    for bingozahl in bingozahlen:
        for feld in felder:
            feld.addZahl(bingozahl)
            if feld.isFertig():
                if feld.deleted:
                    continue
                feld.deleted = True
                ergfeld = feld

        c = 0
        for feld in felder:
            if feld.deleted:
                c += 1
        if c == len(felder):
            print(ergfeld.getSumme() * bingozahl)
            break

    print(f"Programm Ende: {datetime.now()}")