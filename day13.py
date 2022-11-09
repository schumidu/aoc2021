from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    lines = readListFromFile('daten.txt')
    firstHalf = True
    dots = []
    instructions = []
    for line in lines:
        if line == '':
            firstHalf = False
            continue
        if firstHalf:
            dots.append(tuple(map(lambda x: int(x), line.split(','))))
        else:
            instructions.append(line.split(' ')[-1])

    #print(dots)
    #print(instructions)
    for instruction in instructions:
        newdots = []
        splitline = int(instruction.split('=')[1])
        #print(splitline)
        for dot in dots:
            #print(dot)
            nd = None
            if 'x' in instruction and dot[0] > splitline:
                nd = (splitline - (dot[0] - splitline), dot[1])
                newdots.append(nd)
            elif not 'x' in instruction and dot[1] > splitline:
                nd = (dot[0], splitline - (dot[1] - splitline))
                newdots.append(nd)
            else:
                newdots.append(dot)
        dots = list(dict.fromkeys(newdots))
    #Dots anzeigen
    print(dots)
    print(max(list(zip(*dots))[1]))
    for y in range(max(list(zip(*dots))[1])+1):
        for x in range(max(list(zip(*dots))[0])+1):
            if (x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()
    
    print(len(dots))
    print(f"Programm Ende: {datetime.now()}")