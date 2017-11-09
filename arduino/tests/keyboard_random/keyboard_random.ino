
#define KEY_H 11
uint8_t buf[8] = { 
  0 };  
void setup() 
{
  Serial.begin(9600);
  randomSeed(analogRead(0));
  delay(200);
}

void loop() 
{
 

  char modifiers[] = {0x02, 0, 0, 0, 0, 0, 0, 0x02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
  char string[] = {11, 8, 15, 15, 18, 54, 44, 0x0C, 52, 0x10, 0x2C, 0x04, 0x2C, 0x0B, 0x04, 0x06, 0x0E, 0x08, 0x15};

  for (int i = 0; i < sizeof(string); i++) {
    buf[0] = modifiers[i];
    buf[2] = string[i];
    Serial.write(buf, 8);
    delay(30);
    releaseKey();
     delay(30);
  }
  delay(10000);
  
}

void releaseKey() 
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8); // Release key  
}
