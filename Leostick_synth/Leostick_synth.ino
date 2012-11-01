/*
	Leostick Serial controlled annoyance generator.
	
	Copyright (C) 2012 Mark Jessop <mark.jessop@adelaide.edu.au>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For a full copy of the GNU General Public License, 
    see <http://www.gnu.org/licenses/>.
*/

int id = 0;
unsigned int currentFreq = 1000;

void setup(){
  Serial.begin(9600);
  while(!Serial);
  pinMode(11, OUTPUT);
  pinMode(13, OUTPUT);
  //setTone(1568);
  Serial.print("ID");
Serial.print(id);
Serial.println("\n");
}

String inputBuffer = "";
boolean stringComplete = false;
unsigned int count = 0;

void loop(){
	while (Serial.available()) {
		digitalWrite(13,HIGH);
		// Read in a byte.
		char inChar = (char)Serial.read();
		
		// Work out what the character is. If letters or numbers, add to
		// the buffer, if not, don't add.
		
		// If character is a semicolon, we have reached the end of the string.
		if(inChar == '\n'){
			stringComplete = true;
			// Parse string
			break;
		}else if(isalnum(inChar)){
			// Add to the input buffer.
			inputBuffer += inChar;
		}
		
	}
	if(stringComplete){
		stringComplete = false;
		parseCommand(inputBuffer);
		inputBuffer = "";
	}
}


// serialEvent doesn't work with Arduino Leonardo!!!
// This bug was raised in September 2012 and STILL isn't fixed!
// http://code.google.com/p/arduino/issues/detail?id=1031
/*
void serialEvent(){
	while (Serial.available()) {
		digitalWrite(13,HIGH);
		// Read in a byte.
		char inChar = (char)Serial.read();
		
		// Work out what the character is. If letters or numbers, add to
		// the buffer, if not, don't add.
		
		// If character is a semicolon, we have reached the end of the string.
		if(inChar == '\n'){
			stringComplete = true;
			// Parse string
			break;
		}else if(isalnum(inChar)){
			// Add to the input buffer.
			inputBuffer += inChar;
		}
		
	}
	digitalWrite(13,LOW);
}
*/
void parseCommand(String input){
	if(input.length()==2){ // Get Request
		if(input.startsWith("FR")){
			Serial.print("FR");
			Serial.print(currentFreq);
			Serial.print("\n");
		}
		if(input.startsWith("ID")){
			Serial.print("ID");
			Serial.print(id);
			Serial.println("\n");
		}
		if(input.startsWith("ON")){
			setTone(currentFreq);
			Serial.print("OK\n");
		}
		if(input.startsWith("OF")){
			setTone(0);
			Serial.print("OK\n");
		}
		
	
	}else{

		if(input.startsWith("FR")){
			// Set VFO A Command
			setFreq(input.substring(2));
		}
	}
}

void setFreq(String value){
	char s[20];
	value.toCharArray(s,20);
	
	unsigned long l_value = 0;
	l_value = strtoul(s,NULL,10);
	if(l_value>50 && l_value<20000){
		currentFreq = (unsigned int)l_value;
		setTone(currentFreq);
		Serial.print("OK\n");
	}
}
