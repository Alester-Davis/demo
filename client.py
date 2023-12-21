# import socket

# addr = ("127.0.0.1",3003)
# socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# socket.connect(addr)


# inp = input("Client message : ").encode('utf-8')
# socket.send(inp)
# recv,_=socket.recvfrom(100)
# print("Server echo : ",recv.decode('utf-8'))


# import socket

# addr = ("127.0.0.1",3003)
# socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.connect(addr)

# with open('file4.txt','wb') as file:
#     data = socket.recv(1024)
#     while data:
#         file.write(data)
#         data = socket.recv(1024)

addr = ("127.0.0.1",3003)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect(addr)

inp = input("Client message : ").encode('utf-8')
socket.send(inp)
msg = socket.recv(1024).decode('utf-8')
print("Server echo : ",)


