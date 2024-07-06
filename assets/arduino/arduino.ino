// Used to connect the servos to the arduino, which will in turn be used by the raspberry pi to connect to the servos

#include <Servo.h>

// Servos
Servo top;  // Top servo
Servo mid;  // Middle servo
Servo btm;  // Bottom servo

// PWN pins
const int topPin = 8;
const int midPin = 9;
const int btmPin = 10;

void setup() {
  top.attach(topPin);  // Attach top servo to pin
  mid.attach(midPin);  // Attach middle servo to pin
  btm.attach(btmPin);  // Attach bottom servo to pin
}

void loop() {
  // Main code
}
