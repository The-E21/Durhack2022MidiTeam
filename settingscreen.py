import sys
import pygame
from pygame import Rect
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.dropdown import Dropdown


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255, 204, 203)
DARK_RED = (220,20,50)
BLUE = (0, 0, 255)
GREY = (194, 196, 194)
DARK_GREY = (90, 91, 90)

def showSettings():
    pygame.init()


    monitorInfoObject = pygame.display.Info()
    windowWidth: int = monitorInfoObject.current_w
    windowHeight: int = monitorInfoObject.current_h
    scale: float = (windowHeight * windowWidth) / (1920 * 1080)

    titleFont=pygame.font.SysFont('timesnewroman', round(100 * scale))
    subheadingFont=pygame.font.SysFont('timesnewroman', round(50 * scale))
    bodyFont=pygame.font.SysFont('timesnewroman', round(30 * scale))

    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((windowWidth, windowHeight))


    # pygame.display.set_caption("")
    # pygame.display.set_icon(pygame.image.load('resources/logo.png'))

    timer: int = 0



    sliderMaster = Slider(windowSurface, int(windowWidth/13), 100, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputMaster = TextBox(windowSurface, sliderMaster.getX()+sliderMaster.getWidth()+80, sliderMaster.getY(), 50, 50, fontSize=30)
    outputMaster.disable()

    sliderMusic = Slider(windowSurface, int(windowWidth/13), 150, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputMusic = TextBox(windowSurface, sliderMusic.getX()+sliderMusic.getWidth()+80, sliderMusic.getY(), 50, 50, fontSize=30)
    outputMusic.disable()

    sliderPiano = Slider(windowSurface, int(windowWidth/13), 200, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputPiano = TextBox(windowSurface, sliderPiano.getX()+sliderPiano.getWidth()+80, sliderPiano.getY(), 50, 50, fontSize=30)
    outputPiano.disable()

    f=open("resources/settings.txt")
    values=f.readlines()
    f.close()
    for i in range(len(values)):
        values[i]=values[i].strip()
    sliderMaster.setValue(int(values[0]))
    sliderMusic.setValue(int(values[1]))
    sliderPiano.setValue(int(values[2]))
    selected=values[3]


    while True:
        windowSurface.fill(WHITE)

        return_button: Rect = pygame.Rect(15, 8*windowHeight/9-15, windowWidth/9, windowHeight/9)

        easy_button: Rect = pygame.Rect(100, 250, windowWidth/9, windowHeight/9)
        normal_button: Rect = pygame.Rect(100, 350, windowWidth/9, windowHeight/9)
        hard_button: Rect = pygame.Rect(100, 450, windowWidth/9, windowHeight/9)


        outputMaster.setText(sliderMaster.getValue())
        outputMusic.setText(sliderMusic.getValue())
        outputPiano.setText(sliderPiano.getValue())

        events=pygame.event.get()
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(pygame.mouse.get_pos()):
                    from gui import mainMenu
                    mainMenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(pygame.mouse.get_pos()):
                    selected="easy"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_button.collidepoint(pygame.mouse.get_pos()):
                    selected="normal"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_button.collidepoint(pygame.mouse.get_pos()):
                    selected="hard"
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()

        pygame.draw.rect(windowSurface, LIGHT_RED, return_button)
        pygame.draw.rect(windowSurface, LIGHT_RED, easy_button)
        pygame.draw.rect(windowSurface, LIGHT_RED, normal_button)
        pygame.draw.rect(windowSurface, LIGHT_RED, hard_button)

        if(selected=="easy"):
            pygame.draw.rect(windowSurface, DARK_RED, easy_button)
        elif (selected=="normal"):
            pygame.draw.rect(windowSurface, DARK_RED, normal_button)
        else:
            pygame.draw.rect(windowSurface, DARK_RED, hard_button)

        drawText("Settings",windowSurface,0,0, titleFont)
        drawText("Volume",windowSurface,5,50, subheadingFont)
        drawText("Master:",windowSurface,5,100, subheadingFont)
        drawText("Music:",windowSurface,5,150, subheadingFont)
        drawText("Piano:",windowSurface,5,200, subheadingFont)
        drawText("Difficulty", windowSurface, 5,250, subheadingFont)
        drawText("Easy",windowSurface,easy_button.center[0], easy_button.center[1], subheadingFont)
        drawText("Normal",windowSurface,normal_button.center[0], normal_button.center[1], subheadingFont)
        drawText("Hard",windowSurface,hard_button.center[0], hard_button.center[1], subheadingFont)
        drawText("Return",windowSurface,return_button.center[0], return_button.center[1], subheadingFont)

        f=open("resources/settings.txt","w")
        f.write(outputMaster.getText()+'\n')
        f.write(outputMusic.getText()+'\n')
        f.write(outputPiano.getText()+'\n')
        f.write(selected+'\n')
        f.close()

        pygame_widgets.update(events)
        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=RED):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def main():
    showSettings()

if __name__ == '__main__':
    main()