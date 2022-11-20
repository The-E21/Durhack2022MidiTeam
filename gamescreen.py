import pygame
import sys
from pygame import Rect
from pygame import mixer
import pygame.midi

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
        def __init__(self, x, y, key, noteVal, colour1=LIGHT_GREY, width=100, height=30, colour2=RED):
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
        musicDelayFrames = 8 * fps
    elif settings[3] == "normal\n":
        mixer.music.load("resources/AugmentedSongNormal.wav")
        bps = 11/6
        musicDelayFrames = 6 * fps
    else:
        mixer.music.load("resources/AugmentedSongHard.wav")
        bps = 11/4
        musicDelayFrames = 4.8 * fps
    
    musicVolume = (int(settings[0]) * int(settings[1])) / 10000
    pianoVolume = (int(settings[0]) * int(settings[2])) / 10000
    mixer.music.set_volume(musicVolume)
    print(musicDelayFrames)
    keyboardConnected = True
    heldNotes = []
    
    timer: int = 0
    try:
        midiInp = pygame.midi.Input(pygame.midi.get_default_input_id())
        midiOut = pygame.midi.Output(pygame.midi.get_default_output_id())
    except:
        keyboardConnected = False
    
    map_rect = loadmap("map", windowWidth, keys, multiplier)

    while True:
        windowSurface.fill(WHITE)
        backButton: Rect = pygame.Rect(8*windowWidth/9-15, 15, windowWidth/9, windowHeight/9)
        if(timer == musicDelayFrames):
            mixer.music.play()
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
            rect.x -= multiplier*bps/fps
            for key in keys:
                if key.rect.colliderect(rect) and not key.handled:
                    key.handled = True

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

        drawText("Back", windowSurface, 8*windowWidth/9+15, 40,
                 pygame.font.SysFont('calibri', round(100 * scale)), BLACK)
        
        mainClock.tick(fps)
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

def loadmap(map, windowWidth, keys, m):
    rects = []
    from note_seperator import noteSeperator
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
                        rects.append(pygame.Rect((windowWidth+ m*float(note[0])), y, m*(float(note[1])-float(note[0])), height))
    return rects

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

playGame()