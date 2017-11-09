#include "SdFat.h"
#include <LiquidCrystal.h>

LiquidCrystal lcd(8, 7, 5, 4, 3, 2);
int nextButtonState = 0;

SdFat SD;
int SD_CS_PIN = 10;

int BTN_NEXT_PIN = 6;
int BTN_PLAY_PIN = 9;

File root;
File currentFile;

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
  int currentNextButtonState = digitalRead(BTN_NEXT_PIN);
  
  if (currentNextButtonState != nextButtonState) {
    if (currentNextButtonState == HIGH) {
      currentFile = getNextFile();
      printFileOnLCD(currentFile);
    }
    nextButtonState = currentNextButtonState;
  }
}

void initializeSD()
{
  Serial.println("Initializing SD card...");
  pinMode(SD_CS_PIN, OUTPUT);

  if (SD.begin())
  {
    Serial.println("SD card is ready to use.");
  } else
  {
    Serial.println("SD card initialization failed");
    return;
  }
}

File getNextFile() {
  File entry = root.openNextFile();
  if (!entry) {
    root.rewind();
    entry = root.openNextFile();
  } 
  while (entry.isDir()) {
    entry = root.openNextFile();
  } // TODO: what if there's no file? If there are only folders, this will never stop...
  return entry;
}

void printFileOnLCD(File f) {
  char fileName[16];
  f.getName(fileName, 16);
  lcd.clear();
  lcd.print(fileName);
  lcd.setCursor(0,1);
  lcd.print(f.size());
}






