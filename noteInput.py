import pygame as pg
import pygame.midi
import time

def run(input_id=None, output_id=None):
    pg.init()
    pg.fastevent.init()
    event_get = pg.fastevent.get
    event_post = pg.fastevent.post

    pygame.midi.init()

    if input_id is None:
        input_id = pygame.midi.get_default_input_id()
    
    if output_id is None:
        output_id = pygame.midi.get_default_output_id()
    
    i = pygame.midi.Input(input_id)
    o = pygame.midi.Output(output_id)

    notes = []

    pg.display.set_mode((1, 1))

    going = True
    while going:
        events = event_get()
        for e in events:
            if e.type in [pg.QUIT]:
                going = False
            if e.type in [pg.KEYDOWN]:
                going = False
            if e.type in [pygame.midi.MIDIIN]:
                print(e)
                note = removeNote(notes,e.data1)
                if note != None:
                    o.note_off(note[0],note[1])
                else:
                    o.note_on(e.data1,e.data2)
                    notes.append((e.data1,e.data2))
    
        if i.poll():
            midi_events = i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post(m_e)

    del i
    pygame.midi.quit()

def numToNote(num):
    notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    return notes[num % 12]

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

run()