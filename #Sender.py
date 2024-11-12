#Password

#import imporium

import socket
import time
#The actual code
targetip = "25.44.13.108"

port = 5005

message = input("What would you like to send? ")

time.sleep(0.5)

#THC place
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect((targetip,port))
    print (f"connected to {targetip} : {port}")

    time.sleep(0.5)
    
    print ('You have entered: '+ message)

    sock.sendall(message.encode())
    print (f"Packet sent: {message}")

    time.sleep(0.5)

    ack = sock.recv(1024)
    print(f"Received acknowledgment from receiver: {ack.decode()}")

    time.sleep(0.5)

except socket.error as e:
    print(f"Error: {e}")

finally:
    sock.close()