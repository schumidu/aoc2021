from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

numberdict = {
    'abdfg': 5,
    'acdef': 2,
    'acfg': 3,
    'acf': 7,
    'abcdfg': 9,
    'abdefg': 6,
    'bcdf': 4,
    'abcefg': 0,
    'abcdefg': 8,
    'cf': 1
}

mydict = {
    'a': 'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t'
    }
mydictrev = {
    'z':'a',
    'y':'b',
    'x':'c',
    'w':'d',
    'v':'e',
    'u':'f',
    't':'g',
    ' ':' '
}

def uebereinstimmung(digit1: str, digit2: str)-> int:
    counter = 0
    for i in digit1:
        if i in digit2:
            counter += 1
    return counter

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    lines = readListFromFile('daten.txt')
    lines = list(map(lambda x: x.split(' | '), lines))
    print(lines)

    ergebnisSumme = 0

    for line in lines:
        digitArray = ['']*10 #digit == index
        #bekannte ersetzen
        for digit in line[0].split():
            print(digit)
            if len(digit) == 2:
                digitArray[1] = digit
            elif len(digit) == 3:
                digitArray[7] = digit
            elif len(digit) == 4:
                digitArray[4] = digit
            elif len(digit) == 7:
                digitArray[8] = digit
        #alle anderen ersetzen
        for digit in line[0].split():
            if len(digit) == 5:
                if digitArray[1][0] in digit and digitArray[1][1] in digit: #3 gefunden
                    digitArray[3] = digit
                elif uebereinstimmung(digitArray[4], digit) == 3:#5 gefunden
                    digitArray[5] = digit
                else:
                    digitArray[2] = digit
                pass
            elif len(digit) == 6:
                if digitArray[1][0] in digit and digitArray[1][1] in digit: #0 oder 9
                    if uebereinstimmung(digitArray[4], digit) == 4:
                        digitArray[9] = digit
                    else:
                        digitArray[0] = digit
                    pass
                else:
                    digitArray[6] = digit
        print(digitArray)
        # alle im Ursprung ersetzt jetzt aus nach | zahlen machen
        sum = ''
        for digit in line[1].split():
            for index, zahl in enumerate(digitArray):
                print(zahl)
                print(digit)
                print()
                if sorted(digit) == sorted(zahl):
                    sum += str(index)

        ergebnisSumme += int(sum)            

    print(ergebnisSumme)
    print(f"Programm Ende: {datetime.now()}")
    pass