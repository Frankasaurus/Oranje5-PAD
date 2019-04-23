import socket
import pickle

UDP_IP = "192.168.85.139" # ip adres van de receiver 
UDP_PORT = 5005
a = []
a.append('Haloo')
a.append('client 139')
MESSAGE = pickle.dumps(a)
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
