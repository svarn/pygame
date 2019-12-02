import sys
import os
import pygame
import random
import math
from pygame.locals import *

pygame.init()





# fukcja losowy cel kulki
def los():
    a = [random.randint(0, 500), 0]
    b = [500, random.randint(0, 500)]
    c = [random.randint(0, 500), 500]
    d = [0, random.randint(0, 500)]
    z = random.randint(1, 4)
    if z == 1:
        los_wsp = a
    elif z == 2:
        los_wsp = b
    elif z == 3:
        los_wsp = c
    elif z == 4:
        los_wsp = d
    print("cel kulki: " + str(los_wsp))
    return los_wsp


#  funkcja na losowy kolor kulki
def los_kol():
    z = random.randint(1, 7)
    if z == 1 and kol != bialy:
        return bialy
    if z == 2 and kol != czerwony:
        return czerwony
    if z == 3 and kol != zielony:
        return zielony
    if z == 4 and kol != niebieski:
        return niebieski
    if z == 5 and kol != zolty:
        return zolty
    if z == 6 and kol != fioletowy:
        return fioletowy
    if z == 7 and kol != blekitny:
        return blekitny


# zegar
FPS = 120
fps_clock = pygame.time.Clock()

# region kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)
zielony = (0, 255, 0)
niebieski = (0, 0, 255)
zolty = (255, 255, 0)
fioletowy = (255, 0, 255)
blekitny = (0, 255, 255)
# endregion

# wspolrzedne ekranu
W = 500
H = 500
pol_W = W // 2
pol_H = H // 2

# ekran
EKRAN = pygame.display.set_mode((W, H))
pygame.display.set_caption("kulka")

# region zmienne

j = 0  # zmienna okreslajaca ktory kierunek kulka obierze

kulka_x = pol_W
kulka_y = pol_H  # wspolrzedne kulki

kier_x = 0
kier_y = 0  # przyszle kierunki lotu

r_x = 0
r_y = 0  # przyszłe losowe docelowe wspolrzedne

szybkosc = 3  # szybkosc kulki

p = 10  # promien kulki

kol = bialy  # kolor kulki

timer = 24  # czestotliwosc mozliwosci zmiany koloru

mn = 1.05  # mnoznik przyspieszenia/spowolnienia

# endregion

while True:

    # region eventy: wyjscie, przyspieszanie scrollem
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 4:
                kier_x = kier_x * mn
                kier_y = kier_y * mn
            elif event.button == 5:
                kier_x = kier_x / mn
                kier_y = kier_y / mn
    #  endregion

    # region zmienianie koloru, przyspieszanie strzalkami
    timer += 1
    m = pygame.mouse.get_pressed()
    if m[0] and timer > 24:
        kol = los_kol()
        if kol is None:
            kol = los_kol()
        timer = 0
    elif pygame.key.get_pressed()[K_UP]:
        kier_x = kier_x * mn
        kier_y = kier_y * mn
    elif pygame.key.get_pressed()[K_DOWN]:
        kier_x = kier_x / mn
        kier_y = kier_y / mn
    # endregion

    if j == 0:
        r = los()
        r_x = r[0]
        r_y = r[1]
        j += 1

    if j == 1:
        radiany = math.atan2(r_y - kulka_y, r_x - kulka_x)
        kier_x = math.cos(radiany) * szybkosc
        kier_y = math.sin(radiany) * szybkosc
        j += 1

    if j == 2:
        kulka_x += kier_x
        kulka_y += kier_y
        if kulka_x < p:
            j = 3
        elif kulka_x > W - p:
            j = 3
        elif kulka_y < p:
            j = 4
        elif kulka_y > H - p:
            j = 4

    if j == 3:
        kulka_x -= kier_x
        kulka_y += kier_y
        if kulka_x < p:
            j = 2
        elif kulka_x > W - p:
            j = 2
        elif kulka_y < p:
            j = 5
        elif kulka_y > H - p:
            j = 5

    if j == 4:
        kulka_x += kier_x
        kulka_y -= kier_y
        if kulka_x < p:
            j = 5
        elif kulka_x > W - p:
            j = 5
        elif kulka_y < p:
            j = 2
        elif kulka_y > H - p:
            j = 2

    if j == 5:
        kulka_x -= kier_x
        kulka_y -= kier_y
        if kulka_x < p:
            j = 4
        elif kulka_x > W - p:
            j = 4
        elif kulka_y < p:
            j = 3
        elif kulka_y > H - p:
            j = 3

#    print(kulka_x, kulka_y)
    try:
        pygame.draw.circle(EKRAN, kol, (int(kulka_x), int(kulka_y)), p, 0)
    except TypeError:
        pass
    pygame.display.update()
    fps_clock.tick(FPS)
    EKRAN.fill(czarny)
