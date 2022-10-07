import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=input("enter host")
port = int(input("enter port"))
s.settimeout(5)
def portScanner(port):
    if s.connect_ex((host,port)):
        print("the port is closed")
    else:
        print("the port is open")    
portScanner(port)        

         