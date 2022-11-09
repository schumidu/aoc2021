from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    liste = readListFromFile('daten.txt')
    positions = list(map(lambda x: int(x), liste[0].split(',')))
    print(positions)
    print(len(positions))
    minimum = min(positions)
    maximum = max(positions)
    cost = maximum * len(positions) * 1000000000
    aktkost = 0
    mintarget = 80

    for target in range(minimum, maximum+1):
    #for target in [0, 5]:
        aktcost = 0
        for position in positions:
            n = abs(position - target)
            delta = int((n*(n+1))/2)
            aktkost += delta

        if aktkost < cost:
            cost = aktkost
            aktkost = 0
            mintarget = target

    print(cost)

    print(f"Programm Ende: {datetime.now()}")