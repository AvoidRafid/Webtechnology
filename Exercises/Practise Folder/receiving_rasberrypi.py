import can


def receive_data():
    can_interface = 'can0'  # Adjust based on your setup

    with can.interface.Bus(channel=can_interface, bustype='socketcan') as bus:
        while True:
            message = bus.recv()
            data = message.data.decode('utf-8')
            print(f"Received: {data}")

# Run the data receiving function
receive_data()
