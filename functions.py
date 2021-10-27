from math import pow
import random

def validacion_1 (p):
    if p < 1:
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, p):
            if p % i == 0:
                return False
        return True
    
def maximo_comun_divisor(a,b):
    temporal = 0
    while b !=0:
        temporal = b
        b = a % b
        a = temporal
    if a != 1:
        return False
    else:
        return True


def encriptacion(m,e,n):
    elevado = m**e
    modulo = elevado % n 
    return modulo

def egcd(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = egcd(b % a, a) 
        return (g, x - (b // a) * y, y)

def modinv(a, m): 
    g, x, y = egcd(a, m) 
    if g != 1: 
        return False
    else: 
        return x % m


def desencriptacion(m,n,d):
    elevado = m**d
    modulo = elevado % n
    return modulo

a = random.randint(2, 10) 


# Apartado Elgamal

def gcd(a,b):
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 


def gen_key(q): 
  
    key = random.randint(pow(10, 20), q) 
    while gcd(q, key) != 1: 
        key = random.randint(pow(10, 20), q) 
  
    return key

def power(a, b, c): 
    x = 1
    y = a 
  
    while b > 0: 
        if b % 2 == 0: 
            x = (x * y) % c; 
        y = (y * y) % c 
        b = int(b / 2) 
  
    return x % c 

def encrypt(msg, q, h, g):

    en_msg = [] 
  
    k = gen_key(q)# Private key for sender 
    s = power(h, k, q) 
    p = power(g, k, q) 
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 

def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = power(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 
  