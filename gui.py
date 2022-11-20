import pygame
from pygame import Rect
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 204, 203)
DARK_RED = (220,20,50)
BLUE = (0, 0, 255)
GREY = (194, 196, 194)
DARK_GREY = (90, 91, 90)

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
        scores_button: Rect = pygame.Rect(15, 6.2*windowHeight/11-5, windowWidth/5, windowHeight/9)

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
                if scores_button.collidepoint(pygame.mouse.get_pos()):
                    from highscorescreen import highScoreDisplay
                    highScoreDisplay()

        pygame.draw.rect(windowSurface, LIGHT_RED, quit_button)
        pygame.draw.rect(windowSurface, DARK_RED, quit_button, 10)

        pygame.draw.rect(windowSurface, LIGHT_RED, play_button)
        pygame.draw.rect(windowSurface, DARK_RED, play_button, 10)

        pygame.draw.rect(windowSurface, LIGHT_RED, settings_button)
        pygame.draw.rect(windowSurface, DARK_RED, settings_button, 10)

        pygame.draw.rect(windowSurface, LIGHT_RED, scores_button)
        pygame.draw.rect(windowSurface, DARK_RED, scores_button, 10)

        drawText("Exit", windowSurface, 40, 8*windowHeight/9 + 5,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("Play it", windowSurface, 40, 3*windowHeight/9 + 5,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("Augmented Rhythm", windowSurface, 30, windowHeight/12,
                 pygame.font.SysFont('calibri', round(140 * scale)), BLACK)
        drawText("Settings", windowSurface, 40, 4*windowHeight/9+15,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("High scores", windowSurface, 40, 5.1*windowHeight/9+15,
                 pygame.font.SysFont('calibri', round(90 * scale)), BLACK)

        img = pygame.image.load("resources/treble_clef.png")
        windowSurface.blit(img, (4*windowWidth/9, 2*windowHeight/5))

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