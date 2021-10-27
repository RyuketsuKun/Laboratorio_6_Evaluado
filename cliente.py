import socket
import sys
import functions
import time
# Create a TCP/IP socket
loop = True
while(loop):
        sock = socket.create_connection(('localhost', 10000))
        try:

            # Send data
            print("Ingrese sus valores 'p','q' y 'e'... ")
            print("----------------------------------------")
            time.sleep(2)
            entero = 0
            while(entero == 0):
                try: 
                    print("Para que el programa de cifrado y decifrado funcione correctamente intente ingresar numeros altos de p y q (mayor a 15)")
                    p = int(input("Su valor de p: "))
                    while (not functions.validacion_1(p)):
                        print("Ingrese un valor correcto de p \n (Este debe ser un numero primo)...")
                        print("----------------------------------------")
                        time.sleep(2)
                        p = int(input("Su valor de p: "))
                    q = int(input("Su valor de q: "))
                    while (not functions.validacion_1(q)):
                        print("Ingrese un valor correcto de q \n (Este debe ser un numero primo)...")
                        print("----------------------------------------")
                        time.sleep(2)
                        q = int(input("Su valor de q: "))
                    n = p * q
                    nn = (p-1)*(q-1)
                    try:
                        n = n.to_bytes(2,'big')
                        n = int.from_bytes(n,byteorder='big')
                    except OverflowError:
                        print("Porfavor intente con numeros p y q mas pequeños")
                        continue
                    e = int(input("Su valor de e: "))
                    while (not functions.maximo_comun_divisor(n,e) or (1>e or e>nn) or  not functions.modinv(e,nn)):
                        print(f"Ingrese un valor correcto de e \n (Este debe tener como maximo comun divisor, junto a {n} de 1 y debe ser un numero mayor a 1 y menor a {nn})...")
                        print("----------------------------------------")
                        time.sleep(2)
                        e = int(input("Su valor de e: "))
                    entero = 1
                except ValueError:
                    print("Sus valores deben ser enteros positivos (ej: 3,7,320)")
                    print("----------------------------------------")
                    time.sleep(2)


            print(f"Sus valores publicos son n = {n} y e = {e}")
            print("----------------------------------------")
            time.sleep(2)

            entero = 0
            while(entero == 0):
                try: 
                    mensaje = int(input("Ingrese su mensaje a cifrar ( debe ser un numero ): "))
                    entero = 1

                except ValueError:
                    print("Sus valores deben ser enteros positivos (ej: 3,7,320)")
                    print("----------------------------------------")
                    time.sleep(2)


            d = functions.modinv(e,nn)
            MensajeEncript = functions.encriptacion(mensaje,e,n)
            msj_open =open('mensajeentrada.txt', 'a')
            print("Encriptando mensaje...")
            print("----------------------------------------")
            time.sleep(2)
            print(f"Mensaje escrito en el fichero de entrada: {MensajeEncript}")
            msj_open.write(str(MensajeEncript) + '\n')
            msj_open.close()
            message = b'ok'
            print("----------------------------------------")
            time.sleep(2)
            n = n.to_bytes(2,'big')
            e = e.to_bytes(2,'big')
            d = d.to_bytes(2,'big')
            sock.send(e)
            time.sleep(2)
            sock.send(n)
            time.sleep(2)
            sock.send(d)

            time.sleep(10)

        finally:
            print('Se cierra el socket')
            print("----------------------------------------")
            time.sleep(2)
            sock.close()
