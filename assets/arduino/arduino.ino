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
  float inpTP1 = analogRead(A0) * (5.0 / 1023.0); // Input Voltage #1 for top servo
  float inpTP2 = analogRead(A1) * (5.0 / 1023.0); // Input Voltage #2 for top servo

  float inpMP1 = analogRead(A2) * (5.0 / 1023.0); // Input Voltage #1 for middle servo
  float inpMP2 = analogRead(A3) * (5.0 / 1023.0); // Input Voltage #2 for middle servo
  
  float inpBP1 = analogRead(A4) * (5.0 / 1023.0); // Input Voltage #1 for bottom servo
  float inpBP2 = analogRead(A5) * (5.0 / 1023.0); // Input Voltage #2 for bottom servo

  /* Note that '* (5.0 / 1023.0)' converts the analogue value to a voltage */

  // Handle top
  movementHandler(inpTP1, inpTP2, top);

  // Handle middle
  movementHandler(inpMP1, inpMP2, mid);

  // Handle bottom
  movementHandler(inpBP1, inpBP2, btm);
}

// Servo rotation function
void rotateServo(Servo selServo, int pos) { 
  /*
    Servo selServo = Selected servo to rotate
    int pos = Position (varying from 1-3) to move in, where 1 is left, 2 is middle and 3 is right 
  */
}

// Input to movement conversion function
void movementHandler(float pin1, float pin2, Servo selServo) {
  /*
    float pin1 = First input
    float pin2 = Second input
    Servo selServo = Selected servo
  */

  if (pin1 >= 5 && pin2 >= 5) { // Middle

    rotateServo(selServo, 2);

  } else if (pin1 >= 5) { // Left

    rotateServo(selServo, 1);

  } else if (pin2 >= 5) { // Top

    rotateServo(selServo, 3); 

  }
}
