import socket
import logging, multiprocessing

log = multiprocessing.log_to_stderr()
log.setLevel(logging.INFO)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.150',1234))
s.listen(10)

while True:
    client_socket, address = s.accept()
    log.info(f'Connection from {address} has been established!')
    client_socket.send(bytes("Wellcome to the server!", "utf-8"))
