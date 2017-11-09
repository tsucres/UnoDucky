#include "SdFat.h"
SdFat SD;

//#include <SPI.h>

int CS_PIN = 10;

File file;

#define DEBUG false
 
bool end_of_file = false;

uint8_t buf[8] = { 
  0 }; 
  
void setup() 
{
  
  initializeSD();
  
  Serial.begin(9600);
  delay(200);
}

void loop() 
{
  openFile("test.bin");
  while (!end_of_file) {
    read8Bytes();

    if (buf[0] == 0x07) { // Delay
      uint8_t d[7];
      memcpy(d, &buf[1], 7 * sizeof(uint8_t));
      delay((int)d);
    }
    else {
      Serial.write(buf, 8);
      delay(10);
      releaseKey();
      delay(50);
    }
    
    
  }
  closeFile();
  end_of_file = false;
  
  delay(100000);
  
}

void debug(char const *text) {
  if (DEBUG) {
    Serial.println(text);
  }
}
void initializeSD()
{
  debug("Initializing SD card...");
  pinMode(CS_PIN, OUTPUT);

  if (SD.begin())
  {
    debug("SD card is ready to use.");
  } else
  {
    debug("SD card initialization failed");
    return;
  }
}

void closeFile()
{
  if (file)
  {
    file.close();
    debug("File closed");
  }
}

int openFile(char const *filename)
{
  file = SD.open(filename);
  if (file)
  {
    debug("File opened with success!");
    return 1;
  } else
  {
    debug("Error opening file...");
    return 0;
  }
}

void read8Bytes() {
  int i = 0;
  while (i != 8)
  {
    if (!file.available()) {
      end_of_file = true;
      return;
    }
    
    buf[i] = file.read();
    i++;
  }
}


void releaseKey() 
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8); // Release key  
}
