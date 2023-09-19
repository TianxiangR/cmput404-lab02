import socket
from threading import Thread
from client import get

HOST = ""
PORT = 8002
BUFFER_SIZE = 4096

def handle_connection(conn: socket, t_num: int):
    print(f"Thread {t_num} starts")
    data = conn.recv(BUFFER_SIZE)
    full_client_data = b''

    while data:
        full_client_data += data
        data = conn.recv(BUFFER_SIZE)

    third_party_server_data = get("www.google.com", 80, full_client_data)

    conn.sendall(third_party_server_data)
    conn.close()


def start_server():
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)

        print("Server starts")

        t_num = 0

        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            thread = Thread(target=handle_connection, args=(conn, t_num))
            thread.start()
            thread.join()
            t_num += 1
        
if __name__ == "__main__":
    start_server()