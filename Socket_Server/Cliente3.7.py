import socket
import threading
import socketserver
import time
import asyncio

async def run_scheduler():
    while True:
        await asyncio.sleep(1)
        msj=input("Ingrese Mensaje: ")
        if(msj=='a'):
            print(time.asctime())
        else:
            client(HOST, PORT, msj)

        
def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 9991
    print("Raspberry con los motores.")
    print("""
    PARA ESTA DEMOSTRACIÓN SE INGRESARÁ INFORMACION
    CUMPLIENDO LA FUNCIÓN DE LA PÁGINA.
    """)
    asyncio.run(run_scheduler())

    
   
        
