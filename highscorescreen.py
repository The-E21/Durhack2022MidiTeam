import pygame
import sys
import math

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

def highScoreDisplay():
    timer: int = 0
    while True:
        windowSurface.fill(WHITE)

        return_button: Rect = pygame.Rect(15, 8*windowHeight/9-15, windowWidth/8, windowHeight/8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(pygame.mouse.get_pos()):
                    from gui import mainMenu
                    mainMenu()


        pygame.draw.rect(windowSurface, LIGHT_RED, return_button)
        pygame.draw.rect(windowSurface, DARK_RED, return_button, 10)

        drawText("High Scores",windowSurface,windowWidth/5,windowHeight/9,pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        drawText("Name",windowSurface,windowWidth/5,2*windowHeight/9,pygame.font.SysFont('calibri', round(70 * scale)), BLACK)
        drawText("Score",windowSurface,2*windowWidth/5,2*windowHeight/9,pygame.font.SysFont('calibri', round(70 * scale)), BLACK)
        drawText("Name",windowSurface,3*windowWidth/5,2*windowHeight/9,pygame.font.SysFont('calibri', round(70 * scale)), BLACK)
        drawText("Score",windowSurface,4*windowWidth/5,2*windowHeight/9,pygame.font.SysFont('calibri', round(70 * scale)), BLACK)

        f=open("resources/highScores.txt")
        texts=f.readlines()
        f.close()


        scores = [ [0]*2 for i in range(len(texts))]

        for i in range(len(texts)):
            texts[i]=texts[i].replace('\n','').strip()
            scores[i]=texts[i].replace('\n','').split(',')

        scores=sorted(scores, key=lambda x: int(x[1]), reverse=True)


        x=5
        if(len(texts)<=5):
            x=math.floor(len(texts))
        elif(len(texts)<10):
            x=math.floor(len(texts)/2)

        for i in range(x):
            drawText(scores[i][0], windowSurface, windowWidth/5, (3+i)*windowHeight/9,
                 pygame.font.SysFont('calibri', round(50 * scale)), BLACK)
            drawText(scores[i][1], windowSurface, 2*windowWidth/5, (3+i)*windowHeight/9,
                 pygame.font.SysFont('calibri', round(50 * scale)), BLACK)
            if(len(texts)>5):
                drawText(scores[i+x][0], windowSurface, 3*windowWidth/5, (3+i)*windowHeight/9,
                     pygame.font.SysFont('calibri', round(50 * scale)), BLACK)
                drawText(scores[i+x][1], windowSurface, 4*windowWidth/5, (3+i)*windowHeight/9,
                     pygame.font.SysFont('calibri', round(50 * scale)), BLACK)

        pygame.draw.line(windowSurface,BLACK,(2.625*windowWidth/5,2*windowHeight/9),(2.625*windowWidth/5,8*windowHeight/9))


        drawText("Return", windowSurface, 40, 8*windowHeight/9 + 5,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)


        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=(255, 0, 0)):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

highScoreDisplay()