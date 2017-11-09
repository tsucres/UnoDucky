# Tests 
Every code in the current folder tests a specific part of the circuit.
They should all work with the final circuit, though.

They have to be uploaded on the Arduino and then run in the classical way, using the Arduino IDE.


They all works fine with the default `usbserial-atmega16u2-Uno` firmware, except for the ones specifically testing the HID firmware.


### LCD

The [lcd.ino](lcd.ino) file contains the "hello world" lcd example from the (arduino site)[https://www.arduino.cc/en/Tutorial/HelloWorld].

### SD

The [sd.ino](sd.ino) file tests all the functionalities related to the SD module. It tries to create a file and then writes/reads in it. If everything went right, it should output the following in the serial monitor:

```
Initializing SD card...
SD card is ready to use.
test.txt created successfully.
Writing in the opened file: This is sample text!
File closed
test.txt opened with success!
Reading from test.txt: This is sample text!
File closed
```

### LCD & SD

This should print the filenames of the files on the SD card on the LCD screen. The "next" button (analog pin 6) should allow you to progress through the root directory.

If the LCD and SD tests were successful, there's no apparent reason (except a problem with the AN6 button) for this test to fail.

### Keyboard random

This is a modified version of this [gist](https://gist.github.com/mitchtech/2865205).

It has to be run on top of the HID firmware.

When launched, it should print `Hello, I’m a hacker` on the host computer (prepare a text editor or something before powering it). If the keyboard layout of the host computer is not en_US, you may see something a little different.


