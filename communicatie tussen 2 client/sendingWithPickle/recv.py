import socket
import pickle

UDP_IP = "10.0.0.2" # Ip adres van de receiver
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
  data, addr = sock.recvfrom(1024)
  print ("received message:", data)
  print(pickle.loads(data))
