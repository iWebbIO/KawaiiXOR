import hashlib

def encrypt_message(plaintext, password):
    # Convert plaintext to binary string
    plaintext_bits = ''.join(format(ord(c), '08b') for c in plaintext)
    
    # Split plaintext into chunks of 256 bits
    chunk_size = 256
    plaintext_chunks = [plaintext_bits[i:i+chunk_size] for i in range(0, len(plaintext_bits), chunk_size)]
    
    # XOR first chunk with password
    encrypted_chunks = [int(plaintext_chunks[0], 2) ^ int(''.join(format(ord(c), '08b') for c in password), 2)]
    
    # XOR remaining chunks with hash of previous chunk
    for i in range(1, len(plaintext_chunks)):
        previous_chunk_hash = hashlib.sha256(bytes.fromhex(hex(encrypted_chunks[-1])[2:])).hexdigest()
        encrypted_chunks.append(int(plaintext_chunks[i], 2) ^ int(previous_chunk_hash, 16))
    
    # Convert encrypted chunks to hexadecimal string
    encrypted_hex = ''.join(hex(chunk)[2:].zfill(64) for chunk in encrypted_chunks)
    
    return encrypted_hex


def decrypt_message(encrypted_hex, password):
    # Convert encrypted message to list of integers
    encrypted_chunks = [int(encrypted_hex[i:i+64], 16) for i in range(0, len(encrypted_hex), 64)]
    
    # XOR first chunk with password
    plaintext_chunks = [bin(encrypted_chunks[0] ^ int(''.join(format(ord(c), '08b') for c in password), 2))[2:].zfill(256)]
    
    # XOR remaining chunks with hash of previous chunk
    for i in range(1, len(encrypted_chunks)):
        previous_chunk_hash = hashlib.sha256(bytes.fromhex(hex(encrypted_chunks[i-1])[2:])).hexdigest()
        plaintext_chunks.append(bin(encrypted_chunks[i] ^ int(previous_chunk_hash, 16))[2:].zfill(256))
    
    # Convert plaintext chunks to ASCII string
    plaintext = ''.join([chr(int(chunk[i:i+8], 2)) for chunk in plaintext_chunks for i in range(0, len(chunk), 8)])
    
    return plaintext


cryptchoice = input("1. Encrypt or 2. Decrypt >>> ")
if cryptchoice == "1":
    plaintext = input("Enter plaintext > ")
    password = input("Enter passphrase/password (IS VISIBLE) >>> ")
    # You can set your default password to save yourself the hassle, just replace input with your own password
    # You will also need to do this on the decrypt mode too.
    # Encrypt message
    encrypted_hex = encrypt_message(plaintext, password)
    print("Encrypted message:", encrypted_hex)
elif cryptchoice == "2":
    # Decrypt message
    encrypted_hex = input("Enter encrypted hex > ")
    password = input("Enter passphrase/password (IS VISIBLE) >>> ")
    decrypted_plaintext = decrypt_message(encrypted_hex, password)
    print("Decrypted message:", decrypted_plaintext)
