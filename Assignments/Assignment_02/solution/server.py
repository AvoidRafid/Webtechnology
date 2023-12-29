import socket
import threading

# Sample options for different languages
OPTIONS_DE = [(0, 'zwei Herren aus Verona', '1590/91'),
              (1, 'Ein Sommernachstraum', '1595'),
              (2, 'Die lustigen weiber von Windsor', '1597/98')]
OPTIONS_EN = [(0, 'The two Gentleman of Verona', '1590/91'),
              (1, 'A midsummer night\'s Dream', '1595'),
              (2, 'The Merry wives of Windsor', '1597/98')]

OPTIONS = {0: OPTIONS_EN, 1: OPTIONS_DE}

# Function to prepare HTTP response header
def prepare_http_response(content_type, content_length):
    return f"HTTP/1.1 200 OK\nContent-Type: {content_type}\nContent-Length: {content_length}\n\n"

# Function to handle GET requests
def handle_get_request(request):
    try:
        # Extracting the requested file name from the GET request
        file_name = request.split()[1][1:]

        # Read the content of the requested file
        with open(file_name, 'rb') as file:
            content = file.read()

        content_type = 'text/html' if file_name.endswith('.html') else 'text/javascript'
        return prepare_http_response(content_type, len(content)) + content
    except Exception as e:
        print(f"Error handling GET request: {e}")
        return prepare_http_response('text/plain', 0)  # Respond with an empty body on error

# Function to handle POST requests
def handle_post_request(request):
    try:
        # Simulate processing of POST request and return options in JSON format
        selected_language = int(request.split('\r\n')[-1])
        options = OPTIONS.get(selected_language, [])

        json_options = str(options).replace("'", '"')
        return prepare_http_response('application/json', len(json_options)) + json_options
    except Exception as e:
        print(f"Error handling POST request: {e}")
        return prepare_http_response('text/plain', 0)  # Respond with an empty body on error

# Function to handle client connections
def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request_data}")

    if "GET" in request_data:
        response_data = handle_get_request(request_data)
    elif "POST" in request_data:
        response_data = handle_post_request(request_data)
    else:
        response_data = prepare_http_response('text/plain', 0)  # Respond with an empty body for unsupported requests

    client_socket.send(response_data.encode('utf-8'))
    client_socket.close()

# Function to set up the server and handle connections
def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5600))
    server.listen(5)

    print("Server listening on port 5600...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    run_server()
