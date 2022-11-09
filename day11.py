from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

def printGrid(grid):
    for line in grid:
        for num in line:
            print(f'{num} ', end='')
        print()
    print()

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    #octopuses = list(map(lambda x : [[int(z), False] for z in x], readListFromFile('testdaten.txt')))
    octopuses = list(map(lambda x : [int(z) for z in x], readListFromFile('daten.txt')))
    indexlist = []
    flashes = 0
    printGrid(octopuses)
    def flash(li, ci):
        octopuses[li][ci] += 1
        #Nachbarn extra erhöhen
        nachbarn(li-1, ci-1)
        nachbarn(li-1, ci)
        nachbarn(li-1, ci+1)
        nachbarn(li, ci-1)
        nachbarn(li, ci+1)
        nachbarn(li+1, ci-1)
        nachbarn(li+1, ci)
        nachbarn(li+1, ci+1)

    def nachbarn(li, ci):
        if li < 0 or ci < 0 or li >= len(octopuses) or ci >= len(octopuses[li]):
            return
        octopuses[li][ci] += 1 #extra erhöhen
        if octopuses[li][ci] == 10:
            flash(li, ci)
        return
    steps = 0
    #for step in range(steps):
    while True:
        flashes = 0
        indexlist = []
        steps +=1
    #First, the energy level of each octupus increases by 1
        for li in range(len(octopuses)):
            for ci in range(len(octopuses[li])):
                octopuses[li][ci] += 1

        for li in range(len(octopuses)):
            for ci in range(len(octopuses[ci])):
                if octopuses[li][ci] == 10:
                    indexlist.append([li, ci])
                    #Zünden, Nachbarn bearbeiten
                    #flash(li, ci)
        for element in indexlist:
            flash(element[0], element[1])

        for li in range(len(octopuses)):
            for ci in range(len(octopuses)):
                if octopuses[li][ci] > 9:
                    octopuses[li][ci] = 0
                    flashes += 1
        
        if flashes == 100:
            break
                    
        #printGrid(octopuses)

    print("ERGEBNIS")
    print(steps)
    print(f"Programm Ende: {datetime.now()}")