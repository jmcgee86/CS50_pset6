import cs50
import sys

print("This is the key: ", sys.argv[1])

if len(sys.argv)!=2:
    print ("Usage: python caesar.py key")
else:
    key = int(sys.argv[1])%26
    cipher = ""

    while True:
        print("Plaintext: ", end="")
        plaintext = cs50.get_string()
        if len(plaintext)>0:
            break
    for c in plaintext:
        if c.isalpha()!=True:
            cipher +=c
        elif c.isupper():
            cipher+=chr((((ord(c)-65+key)%26)+65))
        else:
            cipher+=chr((((ord(c)-97+key)%26)+97))
    print("Ciphertext: ", cipher)