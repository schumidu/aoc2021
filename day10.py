from datetime import datetime
from statistics import median

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

def getScoreofChar(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137

def getReverseChar(char):
        if char == ')':
            return '('
        elif char == ']':
            return '['
        elif char == '}':
            return '{'
        elif char == '>':
            return '<'

def getScoreCorruption(line)-> int:
    stack = []

    for char in line:
        print(char)
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            #if len(stack) == 0:
             #   print(line)
              #  return getScoreofChar(char)
            c = stack.pop()
            if not (c == getReverseChar(char)):
                print(f'{line}\t{char}')
                return getScoreofChar(char), stack
    
    return 0, stack

def findScore(x):
    erg = 0
    print(x)
    for c in x[::-1]:
        print(erg)
        erg *= 5
        if c == '(':
            erg += 1
        elif c == '[':
            erg += 2
        elif c =='{':
            erg += 3
        elif c == '<':
            erg += 4
    return erg


if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    #zeilen mit falscher klammerung finden
    lines = readListFromFile('daten.txt')
    lines = list(filter(lambda x : getScoreCorruption(x)[0] == 0, lines))
   # lines = list(map(lambda x: getScoreCorruption(x), lines))

    lines = list(map(lambda x: getScoreCorruption(x)[1], lines))
    lines = list(map(findScore, lines))
    print(lines)
    print(len(lines))

    print(median(lines))
    print(f"Programm Ende: {datetime.now()}")
    pass