#include <LiquidCrystal.h>
#include <string.h>

LiquidCrystal lcd(8, 7, 5, 4, 3, 2);
int nextButtonState = 0;

const char* texts[] = {
  "One",
  "Two",
  "Three",
  "Four"
};

int count = 4;
int i = 0;
void setup() {
  pinMode(6, INPUT);
  
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, world!");

}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  
  // print the number of seconds since reset:
  
  int currentButtonState = digitalRead(6);
  
  if (currentButtonState != nextButtonState) {
    if (currentButtonState == HIGH) {
      lcd.clear();
      lcd.print(texts[i%count]);
      lcd.setCursor(0, 1);
      lcd.print(i);
      i++;
    }
    nextButtonState = currentButtonState;
  }
  
}
