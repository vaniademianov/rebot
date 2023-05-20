#include <VirtualWire.h>

int x_pin = A0;
int y_pin = A1; 
int data_pin = 2;

void setup() {
  vw_set_tx_pin(data_pin);
  vw_setup(2000); 
  Serial.begin(9600);
  Serial.println("here I am");
}

void loop() {
  int x_val = analogRead(x_pin);
  int y_val = analogRead(y_pin);

  char data[6]; //формат ['X', 512, 1023, 'Y', 0, 512, 1]
  data[0] = 'X';
  data[1] = (x_val >> 8) & 0xFF;
  data[2] = x_val & 0xFF;
  data[3] = 'Y';
  data[4] = (y_val >> 8) & 0xFF;
  data[5] = y_val & 0xFF;

  vw_send((uint8_t *)data, sizeof(data));
  vw_wait_tx(); // чекати до закінчення передачі

  delay(50); //чекати 50 мс
}
