import pygame
import sys

pygame.init()

monitorInfoObject = pygame.display.Info()
windowWidth: int = monitorInfoObject.current_w
windowHeight: int = monitorInfoObject.current_h
scale: float = (windowHeight * windowWidth) / (1920 * 1080)

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# pygame.display.set_caption("")
# pygame.display.set_icon(pygame.image.load('logo.png'))

def mainMenu():
    timer: int = 0
    while True:
        windowSurface.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()

        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

mainMenu()