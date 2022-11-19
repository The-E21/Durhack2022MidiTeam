import pygame
from pygame import Rect
import sys

pygame.init()

BLACK: tuple[int, int, int] = (0, 0, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)
RED: tuple[int, int, int] = (255, 0, 0)
LIGHT_RED: tuple[int, int, int] = (255, 204, 203)
DARK_RED: tuple[int, int, int] = (220,20,50)
BLUE: tuple[int, int, int] = (0, 0, 255)
GREY: tuple[int, int, int] = (194, 196, 194)
DARK_GREY: tuple[int, int, int] = (90, 91, 90)

monitorInfoObject = pygame.display.Info()
windowWidth: int = monitorInfoObject.current_w
windowHeight: int = monitorInfoObject.current_h
scale: float = (windowHeight * windowWidth) / (1920 * 1080)

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

# pygame.display.set_caption("")
# pygame.display.set_icon(pygame.image.load('resources/logo.png'))

def mainMenu():
    timer: int = 0
    while True:
        windowSurface.fill(WHITE)

        quit_button: Rect = pygame.Rect(15, 8*windowHeight/9-15, windowWidth/9, windowHeight/9)
        play_button: Rect = pygame.Rect(15, 3*windowHeight/9-15, windowWidth/6, windowHeight/9)
        settings_button: Rect = pygame.Rect(15, 5*windowHeight/11-15, windowWidth/6, windowHeight/9)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.collidepoint(pygame.mouse.get_pos()):
                    terminate()
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    from gamescreen import playGame
                    playGame()
                if settings_button.collidepoint(pygame.mouse.get_pos()):
                    from settingscreen import showSettings
                    showSettings()

        pygame.draw.rect(windowSurface, LIGHT_RED, quit_button)
        pygame.draw.rect(windowSurface, DARK_RED, quit_button, 10)
        
        pygame.draw.rect(windowSurface, LIGHT_RED, play_button)
        pygame.draw.rect(windowSurface, DARK_RED, play_button, 10)

        pygame.draw.rect(windowSurface, LIGHT_RED, settings_button)
        pygame.draw.rect(windowSurface, DARK_RED, settings_button, 10)
        

        drawText("Exit", windowSurface, 40, 8*windowHeight/9 + 5,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("Play it", windowSurface, 40, 3*windowHeight/9 + 5,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("Title", windowSurface, 30, windowHeight/12, 
                 pygame.font.SysFont('calibri', round(140 * scale)), BLACK)
        drawText("Settings", windowSurface, 40, 4*windowHeight/9+15, 
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        
        img = pygame.image.load("resources/treble_clef.png")
        windowSurface.blit(img, (600, 300))

        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=(255, 0, 0)):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

mainMenu()