from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generate a random 256-bit key
def generate_key():
    return os.urandom(32)

# Encrypt a file
def encrypt_file(input_file, output_file, key):
    # Generate a random 128-bit IV (Initialization Vector)
    iv = os.urandom(16)

    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read the input file
    with open(input_file, "rb") as f:
        plaintext = f.read()

    # Pad the plaintext to be a multiple of 16 bytes (AES block size)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Write the IV and ciphertext to the output file
    with open(output_file, "wb") as f:
        f.write(iv + ciphertext)

# Decrypt a file
def decrypt_file(input_file, output_file, key):
    # Read the input file
    with open(input_file, "rb") as f:
        data = f.read()

    # Extract the IV and ciphertext
    iv = data[:16]
    ciphertext = data[16:]

    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    # Write the decrypted data to the output file
    with open(output_file, "wb") as f:
        f.write(plaintext)