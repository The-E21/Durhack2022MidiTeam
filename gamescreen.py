import pygame
import sys
from pygame import Rect
from pygame import mixer

def playGame():
    pygame.init()
    mixer.init()

    WHITE: tuple = (255,255,255)
    LIGHT_GREY: tuple = (211, 211, 211)
    RED: tuple[int, int, int] = (255, 0, 0)
    LIGHT_RED: tuple[int, int, int] = (255, 204, 203)
    DARK_RED: tuple[int, int, int] = (220,20,50)
    BLACK: tuple = (0,0,0)
    monitorInfoObject = pygame.display.Info()
    windowWidth: int = monitorInfoObject.current_w
    windowHeight: int = monitorInfoObject.current_h
    scale: float = (windowHeight * windowWidth) / (1920 * 1080)

    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((windowWidth, windowHeight))

    # pygame.display.set_caption("")
    # pygame.display.set_icon(pygame.image.load('resources/logo.png'))

    class Key():
        def __init__(self, x, y, key, colour1=LIGHT_GREY, width=100, height=30, colour2=RED):
            self.x = x
            self.y = y
            self.colour1 = colour1
            self.colour2 = colour2
            self.key = key
            self.width = width
            self.height = height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            
    keys = [
        Key(5, 22*windowHeight/95, pygame.K_s),
        Key(5, 25*windowHeight/95, pygame.K_d),
        Key(5, 28*windowHeight/95, pygame.K_f),
        Key(5, 31*windowHeight/95, pygame.K_g),
        Key(5, 34*windowHeight/95, pygame.K_h),
        Key(5, 37*windowHeight/95, pygame.K_j),
        Key(5, 40*windowHeight/95, pygame.K_k),
        Key(5, 43*windowHeight/95, pygame.K_l),
        Key(5, 46*windowHeight/95, pygame.K_SEMICOLON),
        Key(5, 49*windowHeight/95, pygame.K_QUOTE),
        Key(5, 52*windowHeight/95, pygame.K_KP_ENTER),
        Key(5, 55*windowHeight/95, pygame.K_1),
        Key(5, 58*windowHeight/95, pygame.K_1),
        Key(5, 61*windowHeight/95, pygame.K_1),
        Key(5, 64*windowHeight/95, pygame.K_1),
        Key(5, 67*windowHeight/95, pygame.K_1),
        Key(5, 70*windowHeight/95, pygame.K_1),
        Key(5, 73*windowHeight/95, pygame.K_1),
        Key(5, 76*windowHeight/95, pygame.K_1),
        
        Key(5, 74.5*windowHeight/95, pygame.K_w, BLACK, 45, 20),
        Key(5, 71.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 65.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 62.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 59.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 53.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 50.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 44.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 41.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 38.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 32.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 29.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),
        Key(5, 23.5*windowHeight/95, pygame.K_e, BLACK, 45, 20),]

    class Note():
        pass

    notes = load("music")
    notes = drawNote(notes, windowSurface)

    timer: int = 0
    while True:
        windowSurface.fill(WHITE)
        backButton: Rect = pygame.Rect(8*windowWidth/9-15, 15, windowWidth/9, windowHeight/9)

        #if timer == notes[0][0]:
        #    pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(pygame.mouse.get_pos()):
                    from gui import mainMenu
                    mainMenu()
        
        k = pygame.key.get_pressed()
        for key in keys:
            if k[key.key]:
                pygame.draw.rect(windowSurface, key.colour2, key.rect)
            else:
                pygame.draw.rect(windowSurface, key.colour1, key.rect)
            pygame.draw.rect(windowSurface, BLACK, key.rect, 1)

        pygame.draw.rect(windowSurface, LIGHT_RED, backButton)
        pygame.draw.rect(windowSurface, DARK_RED, backButton, 10)

        drawText("Back", windowSurface, 8*windowWidth/9+15, 40,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        
        mainClock.tick(50)
        timer += 1
        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=(255, 0, 0)):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def load(map):
    pass

def drawNote(notes, surface):
    pass
