from cryptography.fernet import Fernet

# Load the encryption key (Replace this with your actual key)
encryption_key = b'YOUR_SECRET_KEY_HERE'  # Ensure this is the correct key
cipher = Fernet(encryption_key)

# Read the encrypted file
with open("backup_files.zip.enc", "rb") as enc_file:
    encrypted_data = enc_file.read()

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted file
with open("backup_files.zip", "wb") as dec_file:
    dec_file.write(decrypted_data)

print("✅ Decryption successful! File saved as backup_files.zip")
