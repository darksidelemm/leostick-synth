import math

def print_message(midi):
    if midi.isNoteOn():
	print 'ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity()
    elif midi.isNoteOff():
        print 'OFF:', midi.getMidiNoteName(midi.getNoteNumber())
    elif midi.isController():
        print 'CONTROLLER', midi.getControllerNumber(), midi.getControllerValue()


import rtmidi
from Annoyance import Annoyance
midiin = rtmidi.RtMidiIn()
annoy = Annoyance(['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2'])

ports = range(midiin.getPortCount())
if ports:
    print midiin.getPortName(2)
    midiin.openPort(2)
    while True:
        m = midiin.getMessage(50) # some timeout in ms
        if m != None:
            if m.isNoteOn():
                note = m.getNoteNumber()
                freq = int(math.pow(2.0,((note-69.0)/12.0))*440)
                annoy.startTone(freq)
            if m.isNoteOff():
                note = m.getNoteNumber()
                freq = int(math.pow(2.0,((note-69.0)/12.0))*440)
                annoy.stopTone(freq)
            print_message(m)
else:
    print 'NO MIDI INPUT PORTS!'
