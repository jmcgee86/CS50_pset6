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
        else:
            # cipher += (c-'a'+k
            cipher+=(chr(ord(c)+key%26))
    print("Ciphertext: ", cipher)