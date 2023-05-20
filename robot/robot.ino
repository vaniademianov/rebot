#include <SoftwareSerial.h>
#include <RH_ASK.h>
RH_ASK driver;
const int B1A = 3;
const int B1B = 2;
const int A1A = 33;
const int A1B = 32;
String code = "";
void setup() {
  // initialize serial communication with the computer
  Serial.begin(9600);
  pinMode(B1A, OUTPUT);
  pinMode(B1B, OUTPUT);
  pinMode(A1A, OUTPUT);
  pinMode(A1B, OUTPUT);
  if (!driver.init())
    Serial.println("RadioHead initialization failed");
    
}

void stop_motor(int porta, int portb) {
  digitalWrite(porta, LOW);
  digitalWrite(portb, LOW);
}

void activate_motor(int porta, int portb) {
  digitalWrite(porta, LOW);
  digitalWrite(portb, HIGH);
}
void activate_motor_back(int porta, int portb) {
  digitalWrite(porta, HIGH);
  digitalWrite(portb, LOW);
}

void splitString(String str, char delimiter, String resultArray[], int resultSize) {
  int strIndex = 0;
  int arrayIndex = 0;
  while (strIndex < str.length() && arrayIndex < resultSize) {
    int nextDelimiterIndex = str.indexOf(delimiter, strIndex);
    if (nextDelimiterIndex == -1) {
      nextDelimiterIndex = str.length();
    }
    resultArray[arrayIndex] = str.substring(strIndex, nextDelimiterIndex);
    arrayIndex++;
    strIndex = nextDelimiterIndex + 1;
  }
}
void exec(String code) {
  const int maxCommandCount = 5;
  String commands[maxCommandCount];
  splitString(code, ';', commands, maxCommandCount);

  for (int i = 0; i < maxCommandCount; i++) {
    String elem = commands[i];
    String params[maxCommandCount];
    splitString(elem, ' ', params, maxCommandCount);  // use a different variable for params

    if (elem == "RN") {
      // do nothing
    } else if (elem == "RM") {
      activate_motor(B1A, B1B);
    } else if (elem == "SM") {
      stop_motor(B1A, B1B);
    } else if (elem == "RMB") {
      activate_motor_back(B1A, B1B);
    } else if (elem == "RMA") {
      activate_motor(A1A, A1B);
    } else if (elem == "SMA") {
      stop_motor(A1A, A1B);
    } else if (elem == "RMBA") {
      activate_motor_back(A1A, A1B);
      Serial.println("rmba");
    } else if (params[0] == "WT") {
      int delayTime = params[1].toInt();
      Serial.println(delayTime);
      delay(delayTime);
    }
    else if (elem == "SAM") {
      stop_motor(B1A,B1B);
      stop_motor(A1A,A1B);
    }
  }
}
String readString() {
  String str = "";
  while (true) {
    if (Serial.available()) {
      char c = Serial.read();
      if (c == '*') {
        break;  // termination character found, exit loop
      }
      str += c;  // add character to string
    }
  }
  return str;
}
void loop() {

  if (Serial.available()) {
    String receivedString = readString();
    Serial.println(receivedString);
    if (receivedString == "ACT") {
      exec(code);
    } 
    if (receivedString != "ACT")  {
      code = receivedString;
    }
    // Do something with the received string
  }
  uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];
  uint8_t buflen = sizeof(buf);

  if (driver.recv(buf, &buflen)) {
    uint8_t number = *(uint8_t*)buf;
    Serial.println(number);
    if (number == 1) {
      activate_motor(B1A, B1B);
      activate_motor(A1A, A1B);

    }
    if (number == 0) {
      stop_motor(B1A,B1B);
      stop_motor(A1A,A1B);
    }
    if (number == 2) {
      stop_motor(B1A, B1B);
      activate_motor(A1A,A1B);
    }
    if (number == 3) {
      activate_motor_back(B1A, B1B);
      activate_motor_back(A1A, A1B);
    }
    if (number == 4) {

      stop_motor(A1A,A1B);
      activate_motor(B1A, B1B);
    }
  }
   // B1A A1A
   // B1B A1B
            // 1
          // 4 0 2
          //   3

}
