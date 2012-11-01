#!/usr/bin/env python
# Leostick Polyphonic Synth Library.
# Copyright (C) 2012 Mark Jessop <mark.jessop@adelaide.edu.au>
#
# Handles comms to 3 Leosticks, running the Leostick_synth code, supplied in this repo.
# TODO: Make it work with an arbitary number of Leosticks.

import serial

serial_baud = 9600
defaultports = ['/dev/tty.usbmodemfa1321','/dev/tty.usbmodemfa1331','/dev/tty.usbmodemfa1341']

class Annoyance(object):
    
    tones = [0,0,0]
    def __init__(self, portarray=defaultports):
        if(len(portarray)==3):
            self.s1 = serial.Serial(portarray[0], serial_baud, timeout=1)
            self.s2 = serial.Serial(portarray[1], serial_baud, timeout=1) 
            self.s3 = serial.Serial(portarray[2], serial_baud, timeout=1)

    def singleOff(self,ind):
        if(ind==0):
            self.s1.write("OF\n")
        elif(ind==1):
            self.s2.write("OF\n")
        elif(ind==2):
            self.s3.write("OF\n")

    def allOff(self):
        self.s1.write("OF\n")
        self.s2.write("OF\n")
        self.s3.write("OF\n")
    
    def allOn(self):
        self.s1.write("ON\n")
        self.s2.write("ON\n")
        self.s3.write("ON\n")
        
    def setTones(self,tone1,tone2,tone3):
    	tone1 = "FR"+str(tone1) + "\n"
    	tone2 = "FR"+str(tone2) + "\n"
    	tone3 = "FR"+str(tone3) + "\n"
    	self.s1.write(tone1)
    	self.s2.write(tone2)
    	self.s3.write(tone3)
    
    def setSingle(self,ind,tone):
        tone1 = "FR"+str(tone) + "\n"
        if(ind==0):
            self.s1.write(tone1)
        elif(ind==1):
            self.s2.write(tone1)
        elif(ind==2):
            self.s3.write(tone1)


    def startTone(self,freq):
        if freq in self.tones:
            return
        else:
            try:
                ind = self.tones.index(0)
                self.tones[ind] = freq
                self.setSingle(ind,freq)
            except:
                pass

    def stopTone(self,freq):
       if freq in self.tones:
           ind = self.tones.index(freq)
           print "Found"
           self.tones[ind] = 0
           self.singleOff(ind)
    
    def close(self):
        self.s1.close()
        self.s2.close()
        self.s3.close()
