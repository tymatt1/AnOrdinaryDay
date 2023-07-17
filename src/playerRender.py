import Input
import pygame
import renderHelper as rh
import Assets

draw = True
x = 0
y = 0


def drawCharacter():
    global x, y
    rh.drawImg(Assets.character, (x, y), (200, 150))
    if Input.getKey(pygame.K_w):
        y -= 3
    if Input.getKey(pygame.K_s):
        y += 3
    if Input.getKey(pygame.K_a):
        x -= 3
    if Input.getKey(pygame.K_w):
        x += 3
