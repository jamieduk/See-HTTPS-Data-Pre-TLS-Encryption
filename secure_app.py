#
# secure_app.py TLS server (c) J~Net 2026
#
# python3 secure_app.py
#
#
import socket, ssl

context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

HOST="localhost"
PORT=5413

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)

    with context.wrap_socket(sock, server_side=True) as ssock:
        print(f"Server listening on {PORT} (TLS)...")

        while True:
            conn, addr=ssock.accept()

            with conn:
                print("Connection from:", addr)

                data=conn.recv(4096)
                print("Received encrypted data:", data)
