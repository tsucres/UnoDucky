#include "SdFat.h"
#include <LiquidCrystal.h>
#include <string.h>
#define DEBUG false


LiquidCrystal lcd(8, 7, 5, 4, 3, 2);

SdFat SD;
static const int SD_CS_PIN = 10;

static const int BTN_NEXT_PIN = 6;
static const int BTN_PLAY_PIN = 9;

int btnNextState = 0;
int btnPlayState = 0;

static const int DELAY_B_RELEASE = 10; // How many millis before release
static const int DELAY_A_RELEASE = 30; // How many millis after release

File root;
File currentFile;



void debug(char const *text) {
  if (DEBUG) {
    Serial.println(text);
  }
}


void setup() {
  // Only for debug
  Serial.begin(9600);

  // SD init
  initializeSD();

  // buttons init
  pinMode(BTN_NEXT_PIN, INPUT);
  pinMode(BTN_PLAY_PIN, INPUT);

  // lcd init
  lcd.begin(16, 2);

  // show first file on lcd
  root = SD.open("/");
  currentFile = getNextFile();
  printFileOnLCD(currentFile);
  
}

void loop() {
  int btnPlayCurrentState = digitalRead(BTN_PLAY_PIN);

  if (btnPlayCurrentState != btnPlayState) {
    // Button "Play" pushed
    if (btnPlayCurrentState == HIGH) {
      playCurrentFile();
    }
    btnPlayState = btnPlayCurrentState;
  }

  
  int btnNextCurrentState = digitalRead(BTN_NEXT_PIN);
  if (btnNextCurrentState != btnNextState) {
    // Button "Next" pushed
    if (btnNextCurrentState == HIGH) {
      currentFile = getNextFile();
      printFileOnLCD(currentFile);
    }
    btnNextState = btnNextCurrentState;
  }
}



void initializeSD() {
  /**
   * Initialize SD module
   */
  debug("Initializing SD card...");
  pinMode(SD_CS_PIN, OUTPUT);

  if (SD.begin()) {
    debug("SD card is ready to use.");
  } else {
    debug("SD card initialization failed");
  }
  return;
}

File getNextFile() {
  File entry = root.openNextFile();
  if (!entry) {
    root.rewind();
    entry = root.openNextFile();
  } 
  while (entry.isDir()) {
    entry = root.openNextFile();
  } // TODO: what if there's no file? how to stop?
  return entry;
}

void printFileOnLCD(File f) {
  /**
   * Print filename and size of the specified file 
   * on the initialized lcd screen
   */
  char fileName[16];
  f.getName(fileName, 16);
  lcd.clear();
  lcd.print(fileName);
  lcd.setCursor(0,1);
  lcd.print(f.size());
}


int read8Bytes(char* buf) {
  /**
   * Copy 8 bytes from the current file to the specified buffer.
   * Return the number of bytes successfully read.
   */
  int i = 0;
  while (i != 8)
  {
    if (!currentFile.available()) {
      return i;
    }
    buf[i] = currentFile.read();
    i++;
  }
  return i;
}

void releaseKey(char* buf) 
{
  buf = {0};
  Serial.write(buf, 8); // Release key  
}

void playCurrentFile() {
  /**
   * Output the content of the currently selected 
   * file via the usb port.
   */
  char buf[8] = { 0 };
  while (read8Bytes(buf)) {
    if (buf[0] == 0x07) { // Delay
      uint8_t d[7];
      memcpy(d, &buf[1], 7 * sizeof(uint8_t));
      delay((int)d);
    }
    else {
      Serial.write(buf, 8);
      delay(DELAY_B_RELEASE);
      releaseKey(buf);
      delay(DELAY_A_RELEASE);
    }
  }
  currentFile.seek(0);
    
}




