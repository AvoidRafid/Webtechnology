import can
import time
import serial


def receive_and_send_data(serial_port='/dev/ttyUSB0', baud_rate=9600):
    # Open the serial port for communication with the Arduino
    with serial.Serial(serial_port, baud_rate) as ser:
        while True:
            # Read data from the Arduino
            arduino_data = ser.readline().decode('utf-8').strip()

            # Process and use the received data as needed
            print(f"Received from Arduino: {arduino_data}")

            # Sending data over CAN
            can_interface = 'can0'  # Adjust based on your setup
            with can.interface.Bus(channel=can_interface, bustype='socketcan') as bus:
                message = can.Message(arbitration_id=0x123, data=arduino_data.encode('utf-8'), extended_id=False)
                bus.send(message)

            time.sleep(1)  # Adjust based on your data update frequency

# Run the data receiving and sending function
receive_and_send_data()
