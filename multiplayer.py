import socket
import main


def server_connect():
    sock = socket.socket()
    sock.bind(('localhost', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print("LOG: connected:", addr)
    board = main.Board()
    # conn.close()


def client_connect(arr, ip):
    sock = socket.socket()
    sock.connect((ip, 9090))
    while True:
        sock.send(arr)

        data = sock.recv(1024)
    # sock.close()


def server_send_recv(arr):
    while True:
        data = conn.recv(1024)
        conn.send(arr)
