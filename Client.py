import pygame
import socket
import threading

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()


maps = []
i = 0
j = 0
while i < 32:
    maps.append([])
    while j < 60:
        maps[i].append(str(i * 32) + " " + str(j * 32))

        j += 1
    i += 1
    j = 0



def okrug(x, y):
    if (x % 32) != 0:
        if (x % 32) <= 16:
            x -= x % 32
        elif (x % 32) >= 16:
            x += 32 - (x % 32)
    if (y % 32) != 0:
        if (y % 32) <= 16:
            y -= y % 32
        elif (y % 32) >= 16:
            y += 32 - (y % 32)
    return int(x), int(y)

def clients1(x, y, i, j):
    persons = {}
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(bytes("X: %s, Y: %s , Nick: 3) %s %s" % (x, y, i, j), "utf8"))
    person = sock.recv(1024)
    person = str(person)[2:-1]
    persons.update(eval(person))
    sock.close()
    return persons


def imagepersons(persons,person):
    global maps
    for p in persons:
        gameDisplay.blit(person, (int(list(str(maps[int(persons[p]['y'])][int(persons[p]['x'])]).split(' '))[1])-65,
                                int(list(str(maps[int(persons[p]['y'])][int(persons[p]['x'])]).split(' '))[0])-111))

def imageperson(x, y, person):
    gameDisplay.blit(person, (x-65, y-111))

x = display_width / 2
y = display_height / 2
x = okrug(x, y)[0]
y = okrug(x, y)[1]
#x_x = x
#y_y = y

i = int(y / 32)
j = int(x / 32)
#t1 = threading.Thread(target=clients, args=(x, y))
#t1.start()

crashed = False
massImg = ['a.png', 'b.png', 'c.png']
iterImg = 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONUP:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            x = okrug(x, y)[0]
            y = okrug(x, y)[1]
            crashed1 = False

            if x != int(list(maps[i][j].split(' '))[0]) or y != int(list(maps[i][j].split(' '))[1]):
                while not crashed1:
                    while not crashed1:
                        if iterImg >= 3:
                            iterImg = 0
                        yy = int(list(maps[i][j].split(' '))[0])
                        xx = int(list(maps[i][j].split(' '))[1])

                        if xx == x and yy == y:
                            crashed1 = True
                        gameDisplay.fill(white)

                        imagepersons(clients1(xx, yy, i, j), pygame.image.load(massImg[iterImg]))
                        imageperson(xx, yy, pygame.image.load(massImg[iterImg]))
                        if x == xx:
                            pass
                        elif x < xx:
                            j -= 1
                            iterImg += 1
                        elif x > xx:
                            j += 1
                            iterImg += 1
                        if y == yy:
                            pass
                        elif y < yy:
                            i -= 1
                            iterImg += 1
                        elif y > yy:
                            i += 1
                            iterImg += 1

                        pygame.display.update()
                        clock.tick(10)


    gameDisplay.fill(white)
    imageperson(x, y, pygame.image.load(massImg[0]))
    imagepersons(clients1(x, y, i, j), pygame.image.load(massImg[0]))
    iterImg = 0
    pygame.display.update()
    clock.tick(10)
pygame.quit()
quit()

