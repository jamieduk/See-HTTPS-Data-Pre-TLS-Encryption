#
# TLS login client (c) J~Net 2026
#
# python3 lkogin.py
#
#
#
import socket, ssl

PORT=5413

context=ssl.create_default_context()
context.check_hostname=False
context.verify_mode=ssl.CERT_NONE  # insecure demo mode only

credentials="user:mysecretpassword"

with socket.create_connection(('localhost', PORT)) as sock:
    with context.wrap_socket(sock, server_hostname='localhost') as ssock:
        ssock.sendall(credentials.encode())
        print(f"Sent: {credentials}")
