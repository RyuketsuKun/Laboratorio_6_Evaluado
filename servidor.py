import socket
import sys
import functions
import random
import time
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Iniciando servidor {} en el puerto {}'.format(*server_address))
print("----------------------------------------")
time.sleep(2)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('Esperando una conexion...')
    print("----------------------------------------")
    time.sleep(2)
    connection, client_address = sock.accept()
    try:
        print('conexion realizada desde: ', client_address)
        print("----------------------------------------")
        time.sleep(2)
        # Receive the data in small chunks and retransmit it
        index = 0
        datos = []
        data1 = connection.recv(16)
        data2 = connection.recv(16)
        data3 = connection.recv(16)
        connection.sendall(data1)
        e = int.from_bytes(data1,byteorder='big')
        datos.append(e)
        index = index + 1
    
        connection.sendall(data2)
        n = int.from_bytes(data2,byteorder='big')
        datos.append(n)
        index = index + 1

        connection.sendall(data3)
        n = int.from_bytes(data3,byteorder='big')
        datos.append(n)
        index = index + 1

        print(f"Sus valores son e = {datos[0]} y n = {datos[1]}")
        print("----------------------------------------")
        time.sleep(2)
        msj_open = open("mensajeentrada.txt","r")
        for linea in msj_open.readlines():
            if linea[-1] =="\n":
                linea = linea[:-1]
        print(f"Exito!, su mensaje escrito fue: {linea}")
        print("----------------------------------------")
        msj_open.close()
        time.sleep(2)
        valor = int(linea)
        valorFinal = functions.desencriptacion(valor,datos[1],datos[2])

        print("Desencriptando...")
        print(f"Exito!, su mensaje escrito fue: {valorFinal}")
        print("----------------------------------------")
        msj_open = open("mensajerecibido.txt","a")
        msj_open.write(str(valorFinal) + '\n')
        msj_open.close()

        #Apartado ElGamal
        m = str(valorFinal)
        print("Encriptando mensaje con Elgamal...")
        print("----------------------------------------")
        time.sleep(2)
        q =random.randint(pow(10,20), pow(10,50))
        g =random.randint(2,q)

        key = functions.gen_key(q)
        h = functions.power(g,key,q)

        en_msg, p =functions.encrypt(m,q,h,g)

        dr_msg = functions.decrypt(en_msg,p,key,q)
        dmsg = ''.join(dr_msg)
        dmsg = int(dmsg) 
        print(f"Exito!, su mensaje encriptado es: {en_msg}")
        time.sleep(2)
        print("Desencriptando mensaje con Elgamal...")
        print("----------------------------------------")
        time.sleep(2)
        print(f"Exito!, su mensaje desencriptado es: {dmsg}")


    finally:
        # Clean up the connection
        connection.close()
