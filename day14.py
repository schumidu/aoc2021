from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

def getMapDict(rules):
    di = {}
    di2 = {}
    for r in rules:
        di[r.split()[0]] = r.split()[2]
        di2[r.split()[0]] = 0
    return di, di2

def getCountDict(rules):
    di = {}
    for r in rules:
        b = r.split()[0]
        for c in b:
            if not c in di:
                di[c] = 0
    return di

def fillFirst(startstring, countPairDict, countLetterDict):
    for index in range(len(startstring)-1):
        countLetterDict[startstring[index]] += 1
        #countLetterDict[startstring[index+1]] += 1
        countPairDict[startstring[index]+startstring[index+1]] += 1
    countLetterDict[startstring[-1]] += 1

    return countPairDict, countLetterDict
#def doWorkWithPair(pair: str,)



if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    lines = readListFromFile('daten.txt')
    template = lines.pop(0)
    lines.pop(0)
    rules = lines
    rulesDict, countPairDict = getMapDict(rules)
    countLetterDict = getCountDict(rules)
    countPairDict, countLetterDict = fillFirst(template, countPairDict, countLetterDict)

    schritte = 40
    num = 0
    for tiefenschritt in range(schritte):
        co = countPairDict.copy()
        for pair in co:
            num = co[pair]
            if num == 0: continue
            countPairDict[pair] = countPairDict[pair] - num
            c = rulesDict[pair]
            countLetterDict[c] += num
            countPairDict[pair[0]+c] += num
            countPairDict[c+pair[1]] += num

    print(max(list(countLetterDict.values()))- min(list(countLetterDict.values())))

    print(f"Programm Ende: {datetime.now()}")
    pass