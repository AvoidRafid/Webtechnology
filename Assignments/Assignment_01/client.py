import socket as sock
import threading
host = '127.0.0.1'
port = 5001

client_id = input('Enter your identification: ')

client = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
client.connect(host, port)



def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break

def write():
    while True:
        message = (f'{nickname}: {input(">>")}')
        client.send(message.encode('ascii'))



receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()










'''
def client_programm():
    host = '127.0.0.1'
    port = 50007

    client_socket = socket.socket()
    client_socket.connect((host,port))

    message = input(' -> ')

    with socket.socket() as s:
        while message.lower().strip() != 'shut down':
            s.send(message.encode())
            data = s.recv(1024).decode()

            print('recieved from server: ' + data)

            message = input(' -> ')

        s.close()

if __name__ == '__main__':
    client_programm()





HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello Rafid')
    data = s.recv(1024)
print('Recieved', repr(data))
'''