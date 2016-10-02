1) Upload the code
2) Update the firmware with the Arduino-keyboard-0.3.hex (follow https://www.arduino.cc/en/Hacking/DFUProgramming8U2)

sudo dfu-programmer atmega16u2 erase
sudo dfu-programmer atmega16u2 flash Genuino-usbserial-atmega16u2-Uno-R3.hex 
sudo dfu-programmer atmega16u2 reset

3) Enjoy
4) Reiter step 2 with the official formaware to coeback to an normal arduino


source : 
http://wei48221.blogspot.be/2016/06/arduino-uno-hid-keyboard-joystick-part.html
http://mitchtech.net/arduino-usb-hid-keyboard/

http://www.mindrunway.ru/IgorPlHex/USBKeyScan.pdf


put a script.txt file on on an micro-sd card accessible from the arduino. This file could contain a script that tell the arduino what to type. (see the rubber ducky script langage)

send the collected data on a server (via the attacked pc)

save the colected data on a micro-sd card

manage the languages


special firmware for HID + serial : https://github.com/NicoHood/Hoodloader

Micro sd - Arduino 
https://www.youtube.com/watch?v=sS_oW81NweI

