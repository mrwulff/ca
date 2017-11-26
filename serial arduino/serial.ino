/*
Library examples for TM1638.

Copyright (C) 2011 Ricardo Batista <rjbatista at gmail dot com>

This program is free software: you can redistribute it and/or modify
it under the terms of the version 3 GNU General Public License as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <TM1638.h>

// define a module on data pin 8, clock pin 9 and strobe pin 7
TM1638 module[] = {
  TM1638(6, 7, 5),
  TM1638(6, 7, 84),
};
int incomingByte = 0;   // for incoming serial data

void setup() {
  // display a hexadecimal number and set the left 4 dots
  module[0].clearDisplay();
  module[1].clearDisplay();
 // module[1].setDisplayToString("     5");
  //module[0].setDisplayToString("01234567");
  Serial.begin(115200);
}

void loop() {
  //module[0].clearDisplay();
  //module[1].clearDisplay();

  //module[0].setDisplayToString("  RPM");
  //module[1].setDisplayToString("  5422");
  //delay(1000);

  //module[0].clearDisplay();
  //module[1].clearDisplay();

  
  //module[0].setDisplayToString(" 40.1");
  //module[1].setDisplayToString("  DEEPS");

  

  //delay(1000);
  //  Serial.println("Hello world from Ardunio!"); // write a string


  if (Serial.available() > 0) {
                char data = Serial.read();
                char str[2];
                str[0] = data;
                str[1] = '\0';
                Serial.print(str);
                //delay(1000);

                // read the incoming byte:
                incomingByte = Serial.read();

                // say what you got:
                Serial.print("  I received: ");
                Serial.println(incomingByte);
                module[0].clearDisplay();
                module[0].setDisplayToString(str);
                delay(554440);
        } 



}
