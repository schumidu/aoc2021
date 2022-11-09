from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

#111100011000
if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    filename = 'daten.txt'
    liste = readListFromFile(filename)
    #l = o * co2
    counter0 = 0
    counter1 = 0
    for spalte in range(len(liste[0])):
        counter0 = 0
        counter1 = 0
        for zeile in liste:
            if zeile[spalte] == '0':
                counter0 += 1
            else:
                counter1 += 1
        if counter1 >= counter0:
            liste = list(filter(lambda x: x[spalte]=='1', liste))
        else:
            liste = list(filter(lambda x: x[spalte] == '0', liste))
        if len(liste) == 1:
            break
    oxygen = int(liste[0], 2)
       
    liste = readListFromFile(filename)
    #l = o * co2
    counter0 = 0
    counter1 = 0
    for spalte in range(len(liste[0])):
        counter0 = 0
        counter1 = 0
        for zeile in liste:
            if zeile[spalte] == '0':
                counter0 += 1
            else:
                counter1 += 1
        if counter0 <= counter1:
            liste = list(filter(lambda x: x[spalte]=='0', liste))
        else:
            liste = list(filter(lambda x: x[spalte] == '1', liste))
        if len(liste) == 1:
            break
    co2 = int(liste[0], 2)

    print(oxygen)
    print(co2)
    print(oxygen*co2)
    print(f"Programm Ende: {datetime.now()}")