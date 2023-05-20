#include <RH_ASK.h>
RH_ASK driver;
const int JOYSTICK_X_PIN = A0;
const int JOYSTICK_Y_PIN = A1;

const int JOYSTICK_THRESHOLD = 50;

void setup() {
  Serial.begin(9600);
  pinMode(JOYSTICK_X_PIN, INPUT);
  pinMode(JOYSTICK_Y_PIN, INPUT);
  if (!driver.init())
    Serial.println("RadioHead initialization failed");
}

void loop() {
  int x = analogRead(JOYSTICK_X_PIN);
  int y = analogRead(JOYSTICK_Y_PIN);
  // 1
// 4 0 2
//   3
  if (y < JOYSTICK_THRESHOLD) {
    up();
    send(1);
  }
  else if (y > 1023 - JOYSTICK_THRESHOLD) {
    down();
    send(3);
  }
  else if (x > 1023 - JOYSTICK_THRESHOLD) {
    right();
    send(2);
  }
  else if (x < JOYSTICK_THRESHOLD) {
    left();
    send(4);
  }
  else {
    non();
    send(0);
  }
  delay(200);
}

void send(uint8_t number) {
  driver.send((uint8_t*)&number, sizeof(number));
  driver.waitPacketSent();
  Serial.println(number);
}

void up() {
  Serial.println("Up");
}

void non() {
  Serial.println("None");
}

void down() {
  Serial.println("Down");
}

void right() {
  Serial.println("Right");
}

void left() {
  Serial.println("Left");
}
