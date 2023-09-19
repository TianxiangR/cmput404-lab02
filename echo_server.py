import socket
from threading import Thread

HOST = ""
PORT = 8001
BUFFER_SIZE = 4096

def handle_connection(conn: socket, t_num: int):
    print(f"Thread {t_num} starts")
    data = conn.recv(BUFFER_SIZE)
    full_data = b''

    while data:
        full_data += data
        data = conn.recv(BUFFER_SIZE)

    print(f"Data received:\n{full_data}")

    conn.sendall(full_data)
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