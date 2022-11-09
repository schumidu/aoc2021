from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

tiefe = 0
horizontal = 0
aim = 0
if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    liste = readListFromFile('daten.txt')
    for zeile in liste:
        if zeile.split(' ')[0] == 'forward':
            horizontal += int(zeile.split(' ')[1])
            tiefe += (aim * int(zeile.split(' ')[1]))
        elif zeile.split(' ')[0] == 'down':
            aim += int(zeile.split(' ')[1])
            #tiefe += int(zeile.split(' ')[1])
        else:
            aim -= int(zeile.split(' ')[1])
            #tiefe -= int(zeile.split(' ')[1])

    print(tiefe*horizontal)
    print(f"Programm Ende: {datetime.now()}")