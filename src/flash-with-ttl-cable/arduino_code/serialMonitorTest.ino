#include <SoftwareSerial.h>

SoftwareSerial Serial1(2,3); // RX (on board), TX (on board)


void setup() {

//  //hardware serial
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  //software serial
  Serial1.begin(9600);
  while (!Serial1) {
    ;
  }
  delay(1000);
}

void loop() {
  
  Serial.println("This is Serial via TTL flash");
  delay (250);
  Serial1.println("This is Serial1 via TTL flash");
  delay(2000);
}
