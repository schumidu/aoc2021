from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return list(map(lambda x: int(x), file.read().splitlines()))

if __name__ == '__main__':
    print(f"Programm gestarted {datetime.now()}")
    tiefen = readListFromFile('daten.txt')
    print(tiefen)
    counter = 0
    for i in range(1, len(tiefen)-2):
        if (tiefen[i-1] + tiefen[i] + tiefen[i+1]) < (tiefen[i] + tiefen[i+1] + tiefen[i+2]):
            counter = counter + 1
    print(counter)
    print(f"Programm beendet {datetime.now()}")