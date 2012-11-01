# Leostick Polyphonic Synth controller
# Copyright (C) 2012 Mark Jessop <mark.jessop@adelaide.edu.au>
# 
# This is a quick hack of the rtmidi example code, to send the midi events
# to the Annoyance class, which controls the Leosticks.

import math
import rtmidi
from Annoyance import Annoyance

def print_message(midi):
    if midi.isNoteOn():
	print 'ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity()
    elif midi.isNoteOff():
        print 'OFF:', midi.getMidiNoteName(midi.getNoteNumber())
    elif midi.isController():
        print 'CONTROLLER', midi.getControllerNumber(), midi.getControllerValue()



midiin = rtmidi.RtMidiIn()

# Change this to suit.
annoy = Annoyance(['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2'])

midiport = 2 # This is the USB MIDI controller on my machine.

ports = range(midiin.getPortCount())
if ports:
    print midiin.getPortName(midiport)
    midiin.openPort(midiport)
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
