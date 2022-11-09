from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    #1 -> 7-> 1
    #simulieren nach 80 tagen
    liste = readListFromFile('daten.txt')
    liste = list(map(lambda x: int(x),liste[0].split(',')))
    #print(liste)
    dauer = 256
    fischeProTag = [0]*9

    for element in liste:
        fischeProTag[element] += 1

    print(fischeProTag)
    #print(liste)
    speicher = 0
    for day in range(dauer):
        #print(sum(fischeProTag))
        speicher = fischeProTag[0]
        fischeProTag[0] = fischeProTag[1]
        fischeProTag[1] = fischeProTag[2]
        fischeProTag[2] = fischeProTag[3]
        fischeProTag[3] = fischeProTag[4]
        fischeProTag[4] = fischeProTag[5]
        fischeProTag[5] = fischeProTag[6]
        fischeProTag[6] = fischeProTag[7] + speicher
        fischeProTag[7] = fischeProTag[8]
        fischeProTag[8] = speicher


    print(sum(fischeProTag))
    #print(liste)
    print(f"Programm Ende: {datetime.now()}")