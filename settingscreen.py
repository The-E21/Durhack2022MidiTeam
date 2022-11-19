import sys
import pygame
from pygame import Rect
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


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



    sliderMaster = Slider(windowSurface, 100, 100, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputMaster = TextBox(windowSurface, sliderMaster.getX()+sliderMaster.getWidth()+80, sliderMaster.getY(), 50, 50, fontSize=30)
    outputMaster.disable()

    sliderMusic = Slider(windowSurface, 100, 150, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputMusic = TextBox(windowSurface, sliderMusic.getX()+sliderMusic.getWidth()+80, sliderMusic.getY(), 50, 50, fontSize=30)
    outputMusic.disable()

    sliderPiano = Slider(windowSurface, 100, 200, int(windowWidth/4), int(windowHeight/20), min=0, max=100, step=1)
    outputPiano = TextBox(windowSurface, sliderPiano.getX()+sliderPiano.getWidth()+80, sliderPiano.getY(), 50, 50, fontSize=30)
    outputPiano.disable()

    f=open("settings.txt")
    volumes=f.readlines()
    f.close()
    for i in volumes:
        i=i.strip()
    sliderMaster.setValue(int(volumes[0]))
    sliderMusic.setValue(int(volumes[1]))
    sliderPiano.setValue(int(volumes[2]))


    while True:
        windowSurface.fill((255,255,255))


        return_button: Rect = pygame.Rect(15, 8*windowHeight/9-15, windowWidth/9, windowHeight/9)


        outputMaster.setText(sliderMaster.getValue())
        outputMusic.setText(sliderMusic.getValue())
        outputPiano.setText(sliderPiano.getValue())

        events=pygame.event.get()
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(pygame.mouse.get_pos()):
                    from gui import mainMenu
                    mainMenu()
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()

        pygame.draw.rect(windowSurface, (255, 204, 203), return_button)

        drawText("Settings",windowSurface,0,0, titleFont)
        drawText("Volume",windowSurface,5,50, subheadingFont)
        drawText("Master:",windowSurface,5,100, subheadingFont)
        drawText("Music:",windowSurface,5,150, subheadingFont)
        drawText("Piano:",windowSurface,5,200, subheadingFont)
        drawText("Return",windowSurface,return_button.center[0], return_button.center[1], subheadingFont)

        f=open("settings.txt","w")
        f.write(outputMaster.getText()+'\n')
        f.write(outputMusic.getText()+'\n')
        f.write(outputPiano.getText()+'\n')
        f.close()

        pygame_widgets.update(events)
        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=(255, 0, 0)):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def main():
    showSettings()

if __name__ == '__main__':
    main()