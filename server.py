import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "This is the server for the multithreaded socket!")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 8080)
args = parser.parse_args()

s = socket.socket()

host = socket.gethostname()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, args.port))
s.listen(20)

print("Waiting or connection..")

# Note:
# Server: On New connection
# >> Press Enter

def new_connection(client, connection):
	port = connection[1]
	print(f"New connection is made Client No: {port}!...")

	while True:
		message = input(str('>>'))
		message = message.encode('utf-8')
		client.send(message)
		print("Message sent....")

		message = client.recv(1024)
		if message.decode() == 'exit':
			print(f"The Client No: {port}, has gracefully Diconnected! {message.decode('utf-8')}")
			break

		print(f"Client[{port}]: {message.decode('utf-8')}")

while True:
	try:
		client, addr = s.accept()
		threading._start_new_thread(new_connection,(client, addr))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this.")

s.close()
