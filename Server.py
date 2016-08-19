import socket
import map
import threading
person = {} #'1)': {'x': '30', 'y': '16'}, '2)': {'x': '40', 'y': '28'}
nickset = []
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
mass = map.loadmapsobstacles()

def vudeleniemap(x, y):
    i = 0
    j = 0
    global mass
    resmass = []
    while i < 32:
        resmass.append([])
        while j < 60:
            resmass[i].append(mass[y-16+i][x-30+j])
            j += 1
        i += 1
        j = 0
    return resmass

def personsserch(persons, nickset, myx, myy, mynick):
    res = {}
    for nick in nickset:
        j = myx - 30
        i = myy - 16
        if mynick == nick:
            pass
        else:
            while i < myy+16:
                if i == int(persons[nick]['y']):
                    while j < myx+30:
                        if j == int(persons[nick]['x']):
                                res[nick] = persons[nick]
                        j += 1
                    j = myx - 60
                i += 1
    return res

per_cor_x = 50
per_cor_y = 70

def per_cor(nick, pers, x, y):
    try:
        global per_cor_x
        global per_cor_y
        if int(pers[nick]['x']) > x:
            per_cor_x -= int(pers[nick]['x']) - x
        if int(pers[nick]['x']) < x:
            per_cor_x += x - int(pers[nick]['x'])
        if int(pers[nick]['y']) > y:
            per_cor_y -= int(pers[nick]['y']) - y
        if int(pers[nick]['y']) < y:
            per_cor_y += y - int(pers[nick]['y'])
        print('----------------------------------------------------------')
        print('X1: ', int(pers[nick]['x']), 'X2: ', x, "per_cor_x: ", per_cor_x)
        print('Y1: ', int(pers[nick]['y']), 'Y2: ', y, "per_cor_y: ", per_cor_y)
    except:
        pass

while True:
    conn, addr = sock.accept()
    conn.setblocking(3)
    data = conn.recv(1024)

    nickset.append(list(str(data).split(' '))[6].split("'")[0])
    nickset = list(set(nickset))



    per_cor(str(list(str(data).split(' '))[6].split("'")[0]), person,
            int(list(str(data).split(' '))[8].split("'")[0]), int(list(str(data).split(' '))[7]))

    a = {list(str(data).split(' '))[6].split("'")[0]: {
                'x': list(str(data).split(' '))[8].split("'")[0],
                'y': list(str(data).split(' '))[7]}}
    person.update(a)

    person_point = personsserch(person, nickset,
            int(list(str(data).split(' '))[8].split("'")[0]),
            int(list(str(data).split(' '))[7]),
            list(str(data).split(' '))[6].split("'")[0]
                )
    conn.send(bytes("%s" % person_point, "utf8"))
    conn.close()
