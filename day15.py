from datetime import datetime

n = 5

def readListFromFile(filename):
    with open(filename) as file:
        return [[*map(int, l)] for l in file.read().splitlines()]

def printPath(field, path):
    for y in range(len(field)*n):
        for x in range(len(field[0])*n):
            if (x, y) in path:
                print('#', end='')
            else:
                print('-', end='')
        print()

def valid(point, numbers):
    return point[0] >= 0 and point[1] >= 0 and point[1] < len(numbers)*n and point[0] < len(numbers[0])*n

def getNeighbours(point, numbers):
    return [x for x in [(point[0]-1, point[1]),(point[0]+1, point[1]),(point[0], point[1]-1),(point[0], point[1]+1)] if valid(x, numbers)]

def getValue(point, numbers)->int:
    xp = point[0]
    yp = point[1]
    whd = xp // len(numbers) + yp // len(numbers)
    x = xp % len(numbers)
    y = yp % len(numbers)
    value = numbers[y][x]
    for i in range(whd):
        value += 1
        if value > 9:
            value = 1

    return value

if __name__ == '__main__':
    #720 ist richtig
    print(f"Programm Beginn: {datetime.now()}")
    numbers = readListFromFile('daten.txt')
    start = (0, 0)
    abstand = {}
    vorgaenger = {}

    for y in range(len(numbers)*n):
        for x in range(len(numbers[0])*n):
            abstand[(x, y)] = 10**99
            vorgaenger[(x, y)] = None
  
    abstand[start] = 0
    q = list(abstand.keys())

    while q:
        u = sorted(q, key=lambda x: abstand[x])[0]
        q.remove(u)
        for v in getNeighbours(u, numbers):#in Nachbarn
            if v in q:
                    if abstand[v] > abstand[u] + getValue(u, numbers):
                        abstand[v] = abstand[u] + getValue(u, numbers)
                        vorgaenger[v] = u

    #Pfad erstellen
    b = list(abstand.keys())[-1]
    points = []#finaler Pfad
    while True:
        points.append(b)
        if b == start:
            break
        b = vorgaenger[b]
  
    p = list(map(lambda x: getValue(x, numbers), points))
    print(sum(p[0:-1]))

    print(f"Programm Ende: {datetime.now()}")
    pass