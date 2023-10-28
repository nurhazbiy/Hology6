import os

print('Welcome to my best collections archive')
res = input('What is the secret: ')
secret_val = "kodenuklir2023"
if secret_val == res:
    print('How can you still find my collections!!!!')
    os.system('cat flag.txt')
    print()
else:
    print('Try harder xD!')