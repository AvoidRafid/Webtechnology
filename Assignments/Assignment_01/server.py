import socket as sock
import threading


host = '127.0.0.1'            # local host or address
port = 5001                   # solid port


server = sock.socket(sock.AF_INET, sock.SOCK_STREAM) # family name = sock.AF_INET, Type = sock.SOCKET_STREAM
server.bind((host, port))    # bind host address and port together
server.listen()              # configure how many client the server can listen simultaneously

client_id = {}

# Three methods will be defined: broadcast, handle, receive(combines all method)


def broadcast(msg, sender_id = None):
    for cid, conn in client_id.items():               # cid is the key, conn is the value if connected or not
        if cid != sender_id:                          # sending everyone the message without the sender
            try:
                conn.send(msg)
            except:
                del client_id[cid]


def handle_clients(conn, cid):
    conn.send('welcome to  the Chatroom!\n'.encode()) # sending msg to specific connection

    client_id[cid] = conn                             # saving the cid and conn in the dictionary

    info_message = f'Client {cid} has joined ethe chat room!\n'
    broadcast(info_message.encode(), cid)             # broadcasting to all but the person joined recently

    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            broadcast(msg, cid)

    except:
        pass

    del client_id[cid]

    farewell_msg = f'Client {cid} has left the chat-\n'
    broadcast(farewell_msg)

    conn.close()



def accept_client_connection():
    while True:
        conn, addr = server.accept()
        print(f'New connection from {addr}')

        conn.send('Hello! Please provide your identification: '.encode())
        client_id = conn.recv(1024).decode()

        if client_id:
            print(f'Client {client_id} identifier itself.')

            client_thread = threading.Thread(target=handle_clients, args=(conn, client_id))
            client_thread.start()

accept_thread = threading.Thread(target=accept_client_connection)
accept_thread.start()