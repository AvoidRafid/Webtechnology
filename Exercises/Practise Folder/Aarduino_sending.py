'''
void setup() {
  Serial.begin(9600); // Set the baud rate to match the Raspberry Pi
}

void loop() {
  // Replace this with your actual code to read data from sensors or other sources
  float voltage = 5.0;
  float current = 2.0;
  float power = voltage * current;

  // Send the data over the serial port
  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.print("V, Current: ");
  Serial.print(current);
  Serial.print("A, Power: ");
  Serial.print(power);
  Serial.println("W");

  delay(1000); // Adjust the delay based on your data update frequency
}

'''