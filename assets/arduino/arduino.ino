// Used to connect the servos to the arduino, which will in turn be used by the Raspberry Pi to connect to the servos

#include <Servo.h>

// VARIABLE DEFINITIONS
// Servos
Servo top;  // Top servo
Servo mid;  // Middle servo
Servo btm;  // Bottom servo

// PWN pins
const int topPin = 8;
const int midPin = 9;
const int btmPin = 10;

// Input pins:
/*
  A0,A1 are reserved for the top servo
  A2,A3 are reserved for the middle servo
  A4,A5 are reserved for the bottom servo
*/

// FUNCTIONS
// Main functions
void setup() {
  top.attach(topPin);  // Attach top servo to pin
  mid.attach(midPin);  // Attach middle servo to pin
  btm.attach(btmPin);  // Attach bottom servo to pin
  Serial.begin(115200);
}

void loop() {
  int inpTP1 = analogRead(A0); // Input #1 for top servo
  int inpTP2 = analogRead(A1); // Input #2 for top servo

  int inpMP1 = analogRead(A2); // Input #1 for middle servo
  int inpMP2 = analogRead(A3); // Input #2 for middle servo
  
  int inpBP1 = analogRead(A4); // Input #1 for bottom servo
  int inpBP2 = analogRead(A5); // Input #2 for bottom servo
}

// Servo rotation function
void rotateServo(Servo selServo, int pos) { 
  /*
    Servo selServo = Selected servo to rotate
    int pos = Position (varying from 1-3) to move in, where 1 is left, 2 is middle and 3 is right 
  */
}
