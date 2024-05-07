import rsa
import base64
from tkinter.filedialog import askopenfilename, askdirectory

print("This is an implementation of the RSA algorithm using the RSA library.")

def strength():
    s = int(input("How strong do you want your RSA encryption from 512 to 4096: "))
    while 512 > s or 4096 < s:
        s = int(input("Choose between 512 and 4096: "))                
    print("Note that using strong encryption will take some time to generate keys!")
    print("Generating your Keys...")
    return s

def generateKeys():
    (pubkey, privkey) = rsa.newkeys(strength())
    print("""Where do you want to save your Keys?
            A window will pop up, if you dnt see it switch to it using 'alt + tab'""")
    path = askdirectory()
    with open(f'{path}/publicKey.pem', 'wb') as p:
        p.write(pubkey.save_pkcs1('PEM'))
    with open(f'{path}/privatekey.pem', 'wb') as p:
        p.write(privkey.save_pkcs1('PEM'))


def encrypt(message, key):
    encrypted_message = rsa.encrypt(message.encode('utf-8'), key)
    encoded_message = base64.b64encode(encrypted_message).decode('utf-8')
    return print(encoded_message)

def decrypt(ciphertext, key):
    decrypted_message = rsa.decrypt(ciphertext, key).decode('utf-8')
    return print(decrypted_message)

def importkeys():
    choice = input("""What are you importing? 
Public key (1)
Private key (2): 
Choose: """)
    if choice == "1":
        print("A window will pop up to ask you to choose your public key file.")
        print("Note! If you don't see a window, you can try to switch to it by using 'alt + tab'.")
        pubKey = askopenfilename()
        with open(pubKey, 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        enc = input("Do you want to encrypt a message using the public key you just imported? (Y)es or (N)o : ")
        while enc not in ["Y", "y", "N", "n"]:
            enc = input("Answer with Y or N: ") 
        if enc == "Y" or enc == "y":
            plaintext = input("Enter the clear text here: ")
            encrypted_message = encrypt(plaintext, publicKey)
            return encrypted_message
        else:
            exit()         
    elif choice == "2":
        print("A window will pop up to ask you to choose your private key file.")
        print("Note! If you don't see a window, you can try to switch to it by using 'alt + tab'.")
        privKey = askopenfilename()        
        with open(privKey, 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        enc = input("Do you want to decrypt a message using the private key you just imported? (Y)es or (N)o : ")
        while enc not in ["Y", "y", "N", "n"]:
            enc = input("Answer with Y or N: ") 
        if enc == "Y" or enc == "y":
            todecrypt = input("Enter the encrypted text here: ")
            decrypted_message = decrypt(base64.b64decode(todecrypt), privateKey)
            return decrypted_message
        else:
            exit()
def whatodo():
    c=input("""Choose an option: 
1: Generate keys
2: Import keys then encrypt or decrypt:
    ===>""")
    while c not in ["1","2"]:c=input("the only options are 1 or 2 : ")
    if c == "1":generateKeys()
    else: importkeys()
whatodo()
