import shutil
from cryptography.fernet import Fernet

# Generate an encryption key (Do this only once and store safely)
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = cipher_suite.encrypt(file.read())
    
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as enc_file:
        enc_file.write(encrypted_data)
    
    return encrypted_file_path

def compress_folder(source_folder, output_zip):
    shutil.make_archive(output_zip, 'zip', source_folder)
