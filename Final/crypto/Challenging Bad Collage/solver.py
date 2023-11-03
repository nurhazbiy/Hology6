import os
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import codecs
import numpy

KEY = os.urandom(16)

def dec(ct):
    ct_bytes = codecs.decode(ct, "hex")
    dec = AES.new(KEY, AES.MODE_CBC, KEY).decrypt(ct_bytes)
    return codecs.encode(dec, "hex").decode()

def enc(pt):
    pt_bytes = codecs.decode(pt, "hex")
    enc = AES.new(KEY, AES.MODE_CBC, KEY).encrypt(pt_bytes)
    return codecs.encode(enc, "hex").decode()

def get_flag(key):
    FLAG = os.environ.get("FLAG")
    FLAG = pad(FLAG.encode(), 16)
    key_bytes = codecs.decode(key, "hex")
    print(f'{key_bytes = }')
    print(f'{KEY = }')
    return codecs.encode(FLAG, "hex").decode() if key_bytes == KEY else "Try Again !!"

def menu():
    print('===== Menu =====')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Get flag')
    print('4. Exit')
    choice = int(input('> '))
    return choice

#Solver
from os import urandom
plain_text = urandom(16).hex() * 3
chiper_text = enc(plain_text)
new_dechiper_text = chiper_text[:32]+''.zfill(32)+chiper_text[:32]
# dechiper_text = dec(new_dechiper_text)
dechipered_new_chiper_text = dec(new_dechiper_text)


# newdechipertext1 = chipertext[:32]
# newdechipertext2 = ''.zfill(32)
# newdechipertext3 = dechipertext[-32:]
print(f' {plain_text = }')
print(f' {chiper_text = }')
print(f'{new_dechiper_text = }')
print(f'{dechipered_new_chiper_text = }')

# print(f'{newdechipertext1 = }')
# print(f'{newdechipertext2 = }')
# print(f'{newdechipertext3 = }')

pt = bytes.fromhex(dechipered_new_chiper_text)

# first block
pt1 = pt[:32]
# third block 
pt3 = pt[32:]
iv = ''

for i in range(16):
    iv += hex(pt1[i] ^ pt3[i])
    print(iv.replace('0x', ''))

print(f'{len(iv)}')

if(len(iv) == 32 ):
    print(f'{iv = }')
    key = get_flag(iv)
    key_from_hex = bytes.fromhex(key)
    print(f'{key_from_hex = }')
    
while True:
    try:
        choice = menu()
        if choice == 1:
            pt = (input('plaintext = '))
            ciphertext = enc(pt)
            print(f'{ciphertext = }')
        if choice == 2:
            secret = input('plaintext = ')
            decryptedtext = dec(secret)
            print(f'{decryptedtext = }')
        if choice == 3:
            key = input('plaintext = ')
            key = get_flag(key)
            print(f'{key = }')
        if choice == 4:
            break
    except ValueError:
        print('something error happened.')
        print(f'{ValueError =}')
        break

print('bye.')