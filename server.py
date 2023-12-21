# import socket

# addr = ("",3003)
# socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# socket.bind(addr)

# cli,cliaddr = socket.recvfrom(100)
# print("Client message : ",cli.decode('utf-8'))
# socket.sendto(cli,cliaddr)

# import socket

# addr = ("",3003)
# socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.bind(addr)
# socket.listen(1)

# cli,cliaddr = socket.accept()
# with open('file.txt','rb') as file:
#     data = file.read(1024)
#     while data:
#         cli.send(data)
#         data = file.read(1024)


addr = ("",3003)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(addr)
socket.listen(1)

cli,cliaddr = socket.accept()
msg = cli.recv(1024)
print("CLient message : ",msg.decode('utf-8'))
cli.send(msg)