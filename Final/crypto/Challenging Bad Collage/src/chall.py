import os
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import codecs

KEY = os.urandom(16)

def dec(ct):
    ct_bytes = codecs.decode(ct, "hex")
    dec = AES.new(KEY, AES.MODE_CBC, KEY).decrypt(ct_bytes)
    return codecs.encode(dec, "hex").decode()

def menu():
    print('===== Menu =====')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Get flag')
    print('4. Exit')
    choice = int(input('> '))
    return choice

def enc(pt):
    pt_bytes = codecs.decode(pt, "hex")
    enc = AES.new(KEY, AES.MODE_CBC, KEY).encrypt(pt_bytes)
    return codecs.encode(enc, "hex").decode()

def get_flag(key):
    FLAG = os.environ.get("FLAG")
    FLAG = pad(FLAG.encode(), 16)
    key_bytes = codecs.decode(key, "hex")
    return codecs.encode(FLAG, "hex").decode() if key_bytes == KEY else "Try Again !!"

while True:
    try:
        choice = menu()
        if choice == 1:
            pt = (input('plaintext = '))
            ciphertext = enc(pt)
            print(f'{ciphertext = }')
        if choice == 2:
            enct = input('plaintext = ')
            decryptedtext = dec(enct)
            print(f'{decryptedtext = }')
        if choice == 3:
            key = input('key plaintext = ')
            flag = get_flag(key)
            print(f'{flag = }')
            break
        if choice == 4:
            break
    except:
        print('something error happened.')
        break

print('bye.')