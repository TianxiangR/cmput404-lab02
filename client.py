import socket

BUFFER_SIZE = 4096

def get(host: str, port: int, payload: bytes) -> bytes:
    
    full_response: bytes = b''
    # using IPv6
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        print("Socket created")

        s.connect((host, port))
        s.sendall(payload)
        s.shutdown(socket.SHUT_WR)
        data: bytes = s.recv(BUFFER_SIZE)
  
        while data:
            full_response += data
            data = s.recv(BUFFER_SIZE)
        
        
    return full_response

if __name__ == "__main__":
    # host = "www.google.com"
    host = "localhost"
    port = 8002
    payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    print(get(host, port, payload))
        






