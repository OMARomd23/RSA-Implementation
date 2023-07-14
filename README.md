# RSA Encryption and Decryption

This is a Python implementation of the RSA algorithm using the `rsa` library. The code provides functionalities for generating RSA keys, encrypting messages using public keys, and decrypting messages using private keys.

## Prerequisites

To run this code, make sure you have the following:

- Python 3 installed on your system
- The `rsa` library installed. You can install it using `pip install rsa`

## How to Use

1. Run the code in a Python environment.
2. Choose one of the following options:
   - Option 1: Generate Keys
   - Option 2: Import Keys and Encrypt or Decrypt
3. If you choose to generate keys:
   - Enter the desired strength for your RSA encryption (between 512 and 4096).
   - The code will generate a pair of RSA keys (public and private) and save them as `publicKey.pem` and `privatekey.pem` in the chosen directory.
4. If you choose to import keys and encrypt or decrypt:
   - Select whether you want to import a public key (1) or a private key (2).
   - If importing a public key:
     - Choose the public key file by selecting it from a window that will pop up.
     - If you don't see the window, use 'alt + tab' to switch to it.
     - Choose whether you want to encrypt a message using the imported public key.
       - If you choose to encrypt, enter the plaintext message.
       - The code will encrypt the message using the public key and display the encrypted message.
   - If importing a private key:
     - Choose the private key file by selecting it from a window that will pop up.
     - If you don't see the window, use 'alt + tab' to switch to it.
     - Choose whether you want to decrypt a message using the imported private key.
       - If you choose to decrypt, enter the base64-encoded ciphertext.
       - The code will decrypt the ciphertext using the private key and display the decrypted message.

## Notes

- When generating keys, note that using stronger encryption (larger key size) will take more time to generate the keys.
- The code utilizes the `rsa` library for the RSA encryption and decryption operations.
- The `base64` library is used for encoding and decoding the encrypted message.
- The `tkinter.filedialog` library is used to prompt the user for file selection.
