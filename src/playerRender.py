import Input
import pygame
import renderHelper as rh
import Assets

draw = True
x = 910
y = 0


def drawCharacter():
    global x, y
    rh.drawImg(Assets.character, (x, y), (400, 300))
    if Input.getKey(pygame.K_w):
        y -= 3
    if Input.getKey(pygame.K_s):
        y += 3
    if Input.getKey(pygame.K_a):
        x -= 3
    if Input.getKey(pygame.K_d):
        x += 3