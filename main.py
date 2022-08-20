from math import fabs
from operator import truediv
import pygame
import mapBuilderLoader

pygame.init()
screen = pygame.display.set_mode((500, 500)) # x6.25

maps = []
maps.append(mapBuilderLoader.MapLoader("Map - Start", screen, 6.25))
maps.append(mapBuilderLoader.MapLoader("Map - Middle", screen, 6.25))
maps.append(mapBuilderLoader.MapLoader("Map - End", screen, 6.25))
currentMap = maps[0]
mapNum = 0

start = currentMap.find_tiles_by_tag("start")[0]
end = currentMap.find_tiles_by_tag("end")[0]

littleManImage = pygame.image.load("littleMan.png")
littleMan = littleManImage.get_rect()

littleMan.center = start.rect.center

up = False
down = False
left = False
right = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_a:
                left = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_a:
                left = False

    start = currentMap.find_tiles_by_tag("start")[0]
    end = currentMap.find_tiles_by_tag("end")[0]



    currentMap.display_map()
    currentMap.outline_tile(start, (0, 255, 0), 2)
    currentMap.outline_tile(end, (255, 0, 0), 2)

    littleMan.y += -int(up) + int(down)
    littleMan.x += -int(left) + int(right)



    screen.blit(littleManImage, littleMan)

    if end.collides_with(littleMan.center):
        mapNum += 1
        if mapNum == len(maps):
            mapNum = 0
        currentMap = maps[mapNum]
        start = currentMap.find_tiles_by_tag("start")[0]
        littleMan.center = start.rect.center

    pygame.display.flip()
