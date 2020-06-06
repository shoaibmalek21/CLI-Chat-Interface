import socket
import argparse

parser = argparse.ArgumentParser(description = "This is the client for the multi threaded socket server!")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 8080)
args = parser.parse_args()

s = socket.socket()
host = socket.gethostname()
print(f'Connecting to server on port: {args.port}')
print(f'Welcome to our Server. How may I help you today?')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
	try:
		s.connect((host,args.port))
	except Exception as e:
		raise SystemExit(f"We have failed to connect to host & port: {args.port}")

	while True:
		message = input("Me: ")
		s.send(message.encode('utf-8'))
		if message =='exit':
			print("Goodbye! Thank you for Connecting with us.")
			break
		data = s.recv(1024)
		print(f"The server's response is: {data.decode('utf-8')}")
