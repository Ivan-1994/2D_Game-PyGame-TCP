import threading

def loadmapsobstacles():
    maps = []
    f = open('maps.txt', 'r')
    i = 0
    j = 0
    while i < 300:
        maps.append([])
        while j < 300:
            maps[i].append(''.join(f.readline().split()))

            j += 1
        i += 1
        j = 0
    return maps


def inmapsperson():
    maps = []
    f = open('mapsperson.txt', 'r')
    i = 0
    j = 0
    while i < 10:
        maps.append([])
        while j < 10:
            maps[i].append(''.join(f.readline().split()))

            j += 1
        i += 1
        j = 0
    print(maps)
    return maps

def outmapsperson():
    maps = []
    f = open('mapsperson.txt', 'r')
    i = 0
    j = 0
    while i < 10:
        maps.append([])
        while j < 10:
            maps[i].append(''.join(f.readline().split()))

            j += 1
        i += 1
        j = 0
    print(maps)
    return maps

#t1 = threading.Thread(target=loadmapsobstacles)
#t1.start()
