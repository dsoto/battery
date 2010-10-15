#define BAUD 115200
#define ECHO_TO_SERIAL 1

#include <Wire.h>
#include <Fat16.h>
#include <Fat16util.h> 

SdCard card;
Fat16 file;

const int drainPin = 0;
const int sourcePin = 1;

void setup() {
  Serial.begin(BAUD);
  Wire.begin();
  
  card.init();
  Fat16::init(&card);
  
  // create a new file
  char name[] = "LOGGER00.CSV";
  for (uint8_t i = 0; i < 100; i++) {
    name[6] = i/10 + '0';
    name[7] = i%10 + '0';
    // O_CREAT - create the file if it does not exist
    // O_EXCL - fail if the file exists
    // O_WRITE - open for write only
    if (file.open(name, O_CREAT | O_EXCL | O_WRITE)) break;
  }
  file.writeError = false;
}

void loop() {

    int drainVoltage = analogRead(drainPin);
    int sourceVoltage = analogRead(sourcePin);
    long int time = millis();
    #if ECHO_TO_SERIAL
    Serial.print(time);
    Serial.print(",");
    Serial.print(drainVoltage, DEC);
    Serial.print(",");
    Serial.print(sourceVoltage, DEC);
    Serial.print("\r\n");
    #endif 
    file.print(time);
    file.print(",");
    file.print(drainVoltage);
    file.print(",");
    file.print(sourceVoltage);
    file.println();
    file.sync();

    for (int i=0; i<=30; i++){
      delay(1000);
    }


}
