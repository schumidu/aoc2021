from datetime import datetime
import re

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.numberOfOccurences = 0

    def __repr__(self) -> str:
        return f'({self.x}, {self.y} [{self.numberOfOccurences}])'
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            return NotImplemented

        return self.x == __o.x and self.y == __o.y

    def occoured(self):
        self.numberOfOccurences += 1

class Line:
    def __init__(self, linestring: str) -> None:
        linestring = linestring.replace(' -> ', ',')
        l = linestring.split(',')
        self.startpunkt = Point(int(l[0]), int(l[1]))
        self.endpunkt = Point(int(l[2]), int(l[3]))

    def __repr__(self) -> str:
        return f'{self.startpunkt} -> {self.endpunkt}'

    #range ende noch mit dazu nehmen!!!
    def getLinie(self):
        if self.startpunkt.x == self.endpunkt.x or self.startpunkt.y == self.endpunkt.y:
            yprocessed = False
            step = 1
            if self.startpunkt.y > self.endpunkt.y:
                step = -1
            elif self.startpunkt.y < self.endpunkt.y:
                step = 1
            else:
                step = 0
            if not step == 0:
                yprocessed = True
                for deltay in range(self.startpunkt.y, self.endpunkt.y+step, step):
                    yield Point(self.startpunkt.x, deltay)
        
            if self.startpunkt.x > self.endpunkt.x:
                step = -1
            elif self.startpunkt.x < self.endpunkt.x:
                step = 1
            else:
                step = 0
            if not step == 0:
                for deltax in range(self.startpunkt.x, self.endpunkt.x+step, step):
                    if yprocessed:
                        yprocessed = False
                        continue
                    yield Point(deltax, self.endpunkt.y)
        else:
            step = 1
            if self.startpunkt.x > self.endpunkt.x:
                step = -1                
            for index, delta in enumerate(range(self.startpunkt.x, self.endpunkt.x+step, step)):
                p = None
                if self.startpunkt.y < self.endpunkt.y:
                    p = Point(delta, self.startpunkt.y+index)
                    yield p
                else:
                    p = Point(delta, self.startpunkt.y-index)
                    yield p
    
#immer erst y gehen
if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    zeilen = readListFromFile('daten.txt')
    linien = []
    for zeile in zeilen:
        l = Line(zeile)
        linien.append(l)

    punkte = []
    for linie in linien:
        for punkt in linie.getLinie():
            if punkt in punkte:
                punkte[punkte.index(punkt)].occoured()
            else:
                punkt.occoured()
                punkte.append(punkt)
        
    print("Ergebnis")
    print(len(list(filter(lambda x: x.numberOfOccurences >= 2, punkte))))




    print(f"Programm Ende: {datetime.now()}")