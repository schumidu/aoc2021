from datetime import datetime

def readListFromFile(filename):
    with open(filename) as file:
        return file.read().splitlines()

def isAllowed(node, path):
    if node == 'start' or node == 'end':
        return False
    p = path.copy()
    p = list(filter(lambda x: x.islower() and not x == 'start' and not x == 'end', path))
    p = list(map(lambda x: path.count(x), p))
    return sum(p) == len(p)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        #print(path)
        if node not in path or node.isupper() or isAllowed(node, path):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

if __name__ == '__main__':
    print(f"Programm Beginn: {datetime.now()}")
    connections = list(map(lambda x: x.split('-'), readListFromFile('daten.txt')))
    #print(connections)
    #Graph in Dict einlesen
    graphDict = {}
    for connection in connections:
        p = []
        try:
            p = graphDict.pop(connection[0])
        except KeyError as e:
            graphDict[connection[0]] = [connection[1]]
            #print("Err")
            #print(e)
        else:
            p.append(connection[1])
            graphDict[connection[0]] = p
        
        p = []
        try:
            p = graphDict.pop(connection[1])
        except KeyError as e:
            graphDict[connection[1]] = [connection[0]]
        else:
            p.append(connection[0])
            graphDict[connection[1]] = p

    print(graphDict)

    paths = find_all_paths(graph=graphDict, start='start', end='end')
    paths = sorted(paths, key=len)
    print()
    #for path in paths:
     #   print(path, end='\n\n\n')
    print(len(paths))


    print(f"Programm Ende: {datetime.now()}")
    pass