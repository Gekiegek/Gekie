#list

#Import imporium
from wakeonlan import send_magic_packet
import socket
import time

#actual code

listenip = "0.0.0.0"
listenport = 5005

#list
def task_1():
    print("Executing Task 1...")
    time.sleep(0.5)
    print("Task 1 executed successfully!")

def task_2():
    print("Executing Task 2...")
    time.sleep(0.5)
    print("Task 2 executed successfully!")

def task_3():
    print("Executing Task 3...")
    task_1()
    time.sleep(15.5)
    task_2()
    time.sleep(0.5)
    print("Task 3 executed successfully!")

def task_4():
    print("Executing Task 4...")
    time.sleep(0.5)
    print("Task 4 executed successfully!")



message_task_map = [
    {"message": "PR1", "task": task_1},
    {"message": "PR2", "task": task_2},
    {"message": "PR3", "task": task_3},
    {"message": "PR4", "task": task_4},
]
#More can be added if so needed

def find_task_for_message(received_message):
    for item in message_task_map:
        if received_message == item["message"]:
            return item["task"]
    return None

#The connection
while True:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((listenip,listenport))

    sock.listen(1)

    print(f"listening for connections on {listenip} : {listenport}...")

    time.sleep(0.5)

    conn, addr = sock.accept()
    print (f"connected by {addr}")

    time.sleep(0.5)

    while True:
        #Receiving end
        data = conn.recv(1024)
        if not data:
           print("No data received. Closing connection.")
           break

        
        received_message = data.decode().strip()
        print(f"Received: {received_message}")

        #Data check
        if not received_message:
            print("Empty message received. Skipping.")
            continue

        #Check if the message matches a known task
        task = find_task_for_message(received_message)
        if task:
            print(f"Correct packet received: {received_message}")
            task()  
            ack_message = "Task completed successfully!"
            conn.sendall(ack_message.encode())
            print("Acknowledgement sent back to client.")
        else:
            print("Received unexpected message.")
            conn.sendall(b"Unexpected message received.")

        break
    
    conn.close()
    print ("Connection closed")