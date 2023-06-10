import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet
from NetworkManager import NetworkManager
# with open("apache_access.bib", "r") as file:
#     for line in file: 
#         elements = line.split(" ")
#         transaction = {
#             'ip' : elements[0],
#             'timestamp' : "".join([elements[3].strip("[]"),elements[4].strip("[]")]),
#             'kind_of_petition' : elements[5],
#             'route' : elements[6],
#             'version' : elements[7].strip('"'),
#             'status' : elements[8],
#             'completed_time': elements[9].strip('\n')
#         }
        
"""    
with open("numbers.txt","a") as file: 
   for number in range(16,21):
        file.write(str(number) + "\n")


secret_message = "Hey this is a secret!"
encoded_message = secret_message.encode()
secret_hash= hashlib.sha256(encoded_message)

print(secret_hash.hexdigest())
"""

# def calculate_file_hash(file_path, algorithm='sha256'):
#     """Calculate the hash value of a file using the specified algorithm."""
#     hash_object = hashlib.new(algorithm)
#     with open(file_path, 'rb') as file:
#         while True:
#             data = file.read(4096)  # Read the file in chunks
#             if not data:
#                 break
#             hash_object.update(data)
#     return hash_object.hexdigest()

# def compare_files(file1_path, file2_path):
#     """Compare two files by comparing their hash values."""
#     file1_hash = calculate_file_hash(file1_path)
#     file2_hash = calculate_file_hash(file2_path)
    
#     if file1_hash == file2_hash:
#         print("Files are identical.")
#         print(file1_hash)
#         print(file2_hash) 
#     else:
#         print("Files have changed.")
#         print(file1_hash)
#         print(file2_hash) 
# file1 = 'hacker.txt'
# file2 = 'hack_text.txt'

# compare_files(file1, file2)

# def generate_key():
#     """Generate a new encryption key."""
#     return Fernet.generate_key()

# def encrypt_message(message, key):
#     """Encrypt a message using the provided key."""
#     f = Fernet(key)
#     encrypted_message = f.encrypt(message.encode())
#     return encrypted_message

# def decrypt_message(encrypted_message, key):
#     """Decrypt an encrypted message using the provided key."""
#     f = Fernet(key)
#     decrypted_message = f.decrypt(encrypted_message)
#     return decrypted_message.decode()

# # Usage example
# encryption_key = generate_key()
# message_to_encrypt = "Hello, this is a secret message!"

# encrypted = encrypt_message(message_to_encrypt, encryption_key)

# print("Key", encryption_key)
# print("Encrypted message:", encrypted)

# decrypted = decrypt_message(encrypted, encryption_key)
# print("Decrypted message:", decrypted)



# # Serialize and save the private key
# pem = private_key.private_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PrivateFormat.PKCS8,
#     encryption_algorithm=serialization.NoEncryption()
# )
# with open('private_key.pem', 'wb') as f:
#     f.write(pem)

# # Serialize and save the public key
# pem = public_key.public_bytes(
#     encoding=serialization.Encoding.PEM,
#     format=serialization.PublicFormat.SubjectPublicKeyInfo
# )
# with open('public_key.pem', 'wb') as f:
#     f.write(pem)

# # Generate RSA key pair
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048
# )
# public_key = private_key.public_key()

# # Save private key
# with open('private_key.pem', 'wb') as f:
#     f.write(private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption()
#     ))

# # Load private key
# with open('private_key.pem', 'rb') as f:
#     private_key = serialization.load_pem_private_key(
#         f.read(),
#         password=None
#     )

# data = b"Hello, this is a secret message!"
# ciphertext = public_key.encrypt(
#     data,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )

# # Decrypt ciphertext using the private key
# decrypted_data = private_key.decrypt(
#     ciphertext,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )


# print("Decrypted data:", decrypted_data.decode())

network_manager = NetworkManager()
network_manager.read_file()
network_manager.detect_ip()