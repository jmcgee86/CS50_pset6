import cs50
import sys

if len(sys.argv)!=2:
    print ("Usage: python caesar.py key string")
else:
    key = sys.argv[1]
    keyIndex = 0
    keyLength = len(key)
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
            shiftChar = key[keyIndex].upper()
            shift = ord(shiftChar)-65
            cipher+=chr((((ord(c)-65+shift)%26)+65))
            keyIndex = (keyIndex+1)%keyLength
        else:
            shiftChar = key[keyIndex].lower()
            shift = ord(shiftChar)-97
            cipher+=chr((((ord(c)-97+shift)%26)+97))
            keyIndex = (keyIndex+1)%keyLength
    print("Ciphertext: ", cipher)