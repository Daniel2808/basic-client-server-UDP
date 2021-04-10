import socket
my_dict={}
UDP_IP='0.0.0.0'
UDP_PORT=9999

#create the server
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0);
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr =sock.recvfrom(1024)
    print(addr)
    if addr not in my_dict.values():
        my_dict[data.decode()] =addr
        print(my_dict)
    else :
        print(data.decode().split())
        name,message=data.decode().split()
        if name in my_dict:
            sock.sendto(message.encode(), my_dict[name])
            print("msg send")
        else:
            sock.sendto('No such name'.encode(),addr)










