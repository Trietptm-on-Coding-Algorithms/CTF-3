#1st METHOD

from Crypto.PublicKey import RSA

cipher = #Enter the cipher in decimal number 
n = #Enter n (modulus) in decimal number
e = #Enter e (encryption key)  in decimal number
d = #Enter d (decryption key) in decimal number
p = #Enter p (first prime number) in decimal number
q = #Enter q (second prime number) in decimal number

private_key = RSA.construct((n, e, d))
dsmg = private_key.decrypt(cipher)
print dsmg

#2nd METHOD

#import rsa

#pk = rsa.PrivateKey(n, e, d, p, q)
#rsa.decrypt(cipher, pk)

