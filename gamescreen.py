import pygame
import sys
from pygame import Rect
from pygame import mixer
import pygame.midi
import pygame_widgets
from pygame_widgets.textbox import TextBox
from note_seperator import noteSeperator

def playGame():
    fps = 60
    multiplier = 100
    settingsFile = open("resources/settings.txt")
    settings = settingsFile.readlines()
    settingsFile.close()

    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    pygame.midi.init()
    mixer.init()

    WHITE: tuple = (255,255,255)
    LIGHT_GREY: tuple = (211, 211, 211)
    RED: tuple[int, int, int] = (255, 0, 0)
    BLUE: tuple[int,int,int] = (0,0,255)
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
        def __init__(self, x, y, key, noteVal, colour1=LIGHT_GREY, width=100, height=30, colour2=BLUE):
            self.x = x
            self.y = y
            self.colour1 = colour1
            self.colour2 = colour2
            self.key = key
            self.width = width
            self.height = height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.noteVal = noteVal
            self.handled = False
            self.min = 0

    keys = [
        Key(5, 22*windowHeight/95, pygame.K_s, 79),
        Key(5, 25*windowHeight/95, pygame.K_d, 77),
        Key(5, 28*windowHeight/95, pygame.K_f,76),
        Key(5, 31*windowHeight/95, pygame.K_g,74),
        Key(5, 34*windowHeight/95, pygame.K_h,72),
        Key(5, 37*windowHeight/95, pygame.K_j,71),
        Key(5, 40*windowHeight/95, pygame.K_k,69),
        Key(5, 43*windowHeight/95, pygame.K_l,67),
        Key(5, 46*windowHeight/95, pygame.K_SEMICOLON,65),
        Key(5, 49*windowHeight/95, pygame.K_QUOTE,64),
        Key(5, 52*windowHeight/95, pygame.K_KP_ENTER,62),
        Key(5, 55*windowHeight/95, pygame.K_1,60),
        Key(5, 58*windowHeight/95, pygame.K_1,59),
        Key(5, 61*windowHeight/95, pygame.K_1,57),
        Key(5, 64*windowHeight/95, pygame.K_1,55),
        Key(5, 67*windowHeight/95, pygame.K_1,53),
        Key(5, 70*windowHeight/95, pygame.K_1,52),
        Key(5, 73*windowHeight/95, pygame.K_1,50),
        Key(5, 76*windowHeight/95, pygame.K_1,48),
        Key(5, 44.5*windowHeight/95, pygame.K_e,66, BLACK, 45, 20),
        Key(5, 32.5*windowHeight/95, pygame.K_e,73, BLACK, 45, 20),
        Key(5, 38.5*windowHeight/95, pygame.K_e,70,BLACK, 45, 20),
        Key(5, 29.5*windowHeight/95, pygame.K_e,75, BLACK, 45, 20),
        Key(5, 41.5*windowHeight/95, pygame.K_e,68, BLACK, 45, 20),
        Key(5, 50.5*windowHeight/95, pygame.K_e,63, BLACK, 45, 20),
        Key(5, 53.5*windowHeight/95, pygame.K_e,61, BLACK, 45, 20),
        Key(5, 59.5*windowHeight/95, pygame.K_e,58, BLACK, 45, 20),
        Key(5, 23.5*windowHeight/95, pygame.K_e,78, BLACK, 45, 20),
        Key(5, 74.5*windowHeight/95, pygame.K_w,49, BLACK, 45, 20),
        Key(5, 71.5*windowHeight/95, pygame.K_e,51, BLACK, 45, 20),
        Key(5, 65.5*windowHeight/95, pygame.K_e, 54,BLACK, 45, 20),
        Key(5, 62.5*windowHeight/95, pygame.K_e,56, BLACK, 45, 20),
        ]

    musicDelayFrames = 0
    if settings[3] == "easy\n":
        mixer.music.load("resources/AugmentedMusicEasy.wav")
        bps = 11/9
        time_remaining = 170
    elif settings[3] == "normal\n":
        mixer.music.load("resources/AugmentedSongNormal.wav")
        bps = 11/6
        time_remaining = 120
    else:
        mixer.music.load("resources/AugmentedSongHard.wav")
        bps = 11/4
<<<<<<< HEAD
        musicDelayFrames = 4.8 * fps
        time_remaining = 3

=======
        time_remaining = 80
    
    musicDelayFrames = fps*(windowWidth -  105)//int(multiplier*bps)
    forgiveFrames = 20
>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000
    musicVolume = (int(settings[0]) * int(settings[1])) / 10000
    pianoVolume = (int(settings[0]) * int(settings[2])) / 10000
    mixer.music.set_volume(musicVolume)
    print(musicDelayFrames)
    keyboardConnected = True
    heldNotes = []





    timer: int = 0
    file_added=False
    try:
        midiInp = pygame.midi.Input(pygame.midi.get_default_input_id())
        midiOut = pygame.midi.Output(pygame.midi.get_default_output_id())
    except:
        keyboardConnected = False
<<<<<<< HEAD

    map_rect = loadmap("map", windowWidth, keys, multiplier)

    score = 0
    #name = gameStart(windowSurface, windowWidth, windowHeight, scale)
=======
    
    allNotes = noteSeperator("map")
    print(allNotes)
    (map_rect, x_dict) = loadmap("map", windowWidth, keys, multiplier)

    score = 0

    requireKeys = [False] * 32

>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000
    while True:
        windowSurface.fill(WHITE)

        backButton: Rect = pygame.Rect(8*windowWidth/9-15, 15, windowWidth/9, windowHeight/9)
        if(timer == musicDelayFrames):
            mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(pygame.mouse.get_pos()):
                    mixer.music.stop()
                    from gui import mainMenu
                    mainMenu()
            if event.type in [pygame.midi.MIDIIN]:
                print(event)
                note = removeNote(heldNotes,event.data1)
                if note != None:
                    midiOut.note_off(note[0],note[1])
                else:
                    midiOut.note_on(event.data1,int(event.data2 * pianoVolume))
                    heldNotes.append((event.data1,int(event.data2 * pianoVolume)))
<<<<<<< HEAD

=======
                    rNote = checkRequireNote(event.data1,timer,forgiveFrames,fps,bps,allNotes,musicDelayFrames)
                    if not rNote == -1:
                        score += 10
                        allNotes[event.data1 % 48].remove(rNote)
        
>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000
        if keyboardConnected and midiInp.poll():
            midi_events = midiInp.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, midiInp.device_id)

            for m_e in midi_evs:
                event_post(m_e)

        k = pygame.key.get_pressed()
        heldKeys = []
        for note in heldNotes:
            heldKeys.append(note[0])

        for rect in map_rect:
            pygame.draw.rect(windowSurface,(200,0,0), rect)
            float_x = x_dict[map_rect.index(rect)]
            float_x -= multiplier*bps/fps
            x_dict.update({map_rect.index(rect): float_x})
            rect.x = int(float_x)


        pygame.draw.rect(windowSurface, WHITE, pygame.Rect(0,0,5,windowHeight))

        for key in keys:
            if key.noteVal in heldKeys:
                pygame.draw.rect(windowSurface, key.colour2, key.rect)
                key.handled = False
            else:
                pygame.draw.rect(windowSurface, key.colour1, key.rect)
                key.handled = True
            pygame.draw.rect(windowSurface, BLACK, key.rect, 1)


        pygame.draw.rect(windowSurface, LIGHT_RED, backButton)
        pygame.draw.rect(windowSurface, DARK_RED, backButton, 10)

        drawText("Score: " + str(score), windowSurface, 15, 50,
                  pygame.font.SysFont('calibri', round(80 * scale)), BLACK)
        drawText("Time: " + str(time_remaining), windowSurface, 15, 10,
                 pygame.font.SysFont('calibri', round(80 * scale)), BLACK)
        drawText("Back", windowSurface, 8*windowWidth/9+15, 40,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)

        mainClock.tick(fps)
        timer += 1
        if timer % 60 == 0:
            time_remaining -= 1

        if time_remaining <= 0:
            file_added=gameOver(3000, windowSurface, windowWidth, windowHeight, scale, file_added)

        pygame.display.update()

def terminate():
    pygame.quit()
    sys.exit()

def drawText(text, surface, x, y, font, color=(255, 0, 0)):
    textObject = font.render(text, True, color)
    textRect = textObject.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObject, textRect)

def loadmap(map, windowWidth, keys, m):
    rects = []
    x_dict = {}
    index = 0
    allNotes = noteSeperator(map)
    print(allNotes)
    for noteList in allNotes:
        if len(noteList) != 0:
            for note in noteList:
                print(note)
                for key in keys:
                    if (key.noteVal % 48) == allNotes.index(noteList):
                        y = key.y
                        height = key.height
                        x = float((windowWidth+ m*float(note[0])))
                        rects.append(pygame.Rect((windowWidth+ m*float(note[0])), y, m*(float(note[1])-float(note[0])), height))
                        x_dict.update({index: x})
                        index += 1
    return rects, x_dict

<<<<<<< HEAD
def gameOver(score, surface, windowWidth, windowHeight, scale, file_added):
    f = open("resources/highScores.txt", "a")
=======
def gameOver(score, surface, windowWidth, windowHeight, scale):
    f = open("resources/highScores.txt", "a+")
>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000
    from highscorescreen import findSmallestScore
    min = findSmallestScore()
    if score > int(min):
        surface.fill((0,0,0))
        drawText("Congrats! Your score was: " + str(score), surface, windowWidth/4, windowHeight/2,
<<<<<<< HEAD
                 pygame.font.SysFont('calibri', round(80*scale), (255,0,0)))
        if(file_added==False):
            f.write('\n'+"MRX"+ ','+str(score))
            file_added=True
=======
                 pygame.font.SysFont('calibri', round(120*scale), (255,0,0)))
        name = "test" # INSERT NAME GETTER HERE
        lines = f.readlines()
        for line in lines:
            if min in line:
                parts = line.replace("\n", "").replace(" ", "").split(",")
                parts[0] = name
                parts[1] = score
                outLine = ",".join(parts)
                f.write("\n" + outLine)
>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000
    else:
        surface.fill((0,0,0))
        drawText("Unlucky! Your score was: " + str(score), surface, windowWidth/4, windowHeight/2,
                 pygame.font.SysFont('calibri', round(120*scale)), (255,0,0))
    f.close()
    return file_added

def gameStart(surface, windowWidth, windowHeight, scale):
    surface.fill((0,0,0))
    name=""
    check=False
    while check==False:
        check=True
        drawText("Please enter your name (3 letters): ", surface, windowWidth/4, windowHeight/3*2,
                     pygame.font.SysFont('calibri', round(80*scale), (255,0,0)))
        #textbox = TextBox(surface, windowWidth/4, windowHeight/5*4, 200, 80, fontSize=round(scale*80),
         #             borderColour=(255,0,0), textColour=(255, 0, 0),
          #            onSubmit=lambda name: textbox.getText() if(len(textbox.getText==3)) else(check=False),
           #           radius=10, borderThickness=5)
        pygame_widgets.update(pygame.event.get())
##        f.write(textbox.getText()+','+str(score)+'\n') if(textbox.getText()==3) else (
##                    drawText("Name must be 3 characters", surface,windowWidth/4, windowHeight/3*2.5,
##                 pygame.font.SysFont('calibri', round(80*scale), (255,0,0)),colour=(255,255,255))
##                  )
    return name

def removeNote(notes, noteVal):
    rtn = None
    for i in range(len(notes)):
        if notes[i][0] == noteVal:
            rtn = notes[i]

    if rtn != None:
        notes.remove(rtn)
        return rtn
    else:
        return None

<<<<<<< HEAD
def output():
    pass

=======
def checkRequireNote(note,frame,forgiveframes,fps,bps,allNotes,musicDelayFrames):
    for inote in allNotes[note%48]:
        checkFrame = float(inote[0]) * fps/bps + musicDelayFrames
        if(frame >= checkFrame - forgiveframes) and (frame <= checkFrame + forgiveframes):
            return inote
    
    return -1
>>>>>>> 59def4d7d573872c1ffb5f3d005a3fa5f25d0000

playGame()