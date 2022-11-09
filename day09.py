from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    lines = readListFromFile('daten.txt')
    mins = []
    #print(lines)
    zahlenreihen = []
    for lineindex in range(len(lines)):
        reihe = []
        for spaltenindex in range(len(lines[lineindex])):
            num = int(lines[lineindex][spaltenindex])
            if num == 9:
                reihe.append(9)
            else:
                reihe.append(0)
        zahlenreihen.append(reihe)
    print(zahlenreihen)
    #https://en.wikipedia.org/wiki/Flood_fill

    areasizes = []

    print("Start flood fill")
    for lineindex in range(len(zahlenreihen)):
        for columnindex in range(len(zahlenreihen[lineindex])):
            #print(zahlenreihen)
            #print(f'line{lineindex} column{columnindex}')
            if zahlenreihen[lineindex][columnindex] == 0:
                #print("0 gefunden")
                #start flood fill
                def floodfill(line, column)->int:
                    #ungültige indicy ausfilter
                    if line < 0 or column < 0 or line >= len(zahlenreihen) or column >= len(zahlenreihen[0]):
                        return 0
                    if zahlenreihen[line][column] in [1, 9]:
                        return 0
                    zahlenreihen[line][column] = 1
                    return (1 + floodfill(line-1, column) + floodfill(line+1, column) + floodfill(line, column-1) + floodfill(line, column+1))
                
                areasizes.append(floodfill(lineindex, columnindex))

    print("ERGEBNIS")    
    areasizes = sorted(areasizes)[-3:]
    print(areasizes)
    print(areasizes[0]*areasizes[1]*areasizes[2])

    print(f"Programm Ende: {datetime.now()}")
    pass