import boto3
import os
import zipfile
from cryptography.fernet import Fernet

# AWS S3 Configuration
AWS_ACCESS_KEY = "your-access-key"
AWS_SECRET_KEY = "your-secret-key"
BUCKET_NAME = "your-bucket-name"
S3_FILE_KEY = "backups/encrypted_backup.zip"

# Local paths
DOWNLOAD_PATH = "downloaded_backup.zip"
DECRYPTED_PATH = "decrypted_backup.zip"
EXTRACT_FOLDER = "restored_files"

# Encryption Key (Use the same key that was used for encryption)
ENCRYPTION_KEY = b"your-32-byte-key"  # Ensure this is securely stored and retrieved

def download_from_s3():
    """Download the encrypted and compressed file from S3."""
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    s3.download_file(BUCKET_NAME, S3_FILE_KEY, DOWNLOAD_PATH)
    print(f"Downloaded encrypted backup from S3: {DOWNLOAD_PATH}")

def decrypt_file():
    """Decrypt the downloaded file using Fernet encryption."""
    cipher = Fernet(ENCRYPTION_KEY)
    with open(DOWNLOAD_PATH, "rb") as enc_file:
        encrypted_data = enc_file.read()
    
    decrypted_data = cipher.decrypt(encrypted_data)
    
    with open(DECRYPTED_PATH, "wb") as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"Decrypted backup saved as: {DECRYPTED_PATH}")

def extract_backup():
    """Extract the decrypted zip file."""
    if not os.path.exists(EXTRACT_FOLDER):
        os.makedirs(EXTRACT_FOLDER)
    
    with zipfile.ZipFile(DECRYPTED_PATH, "r") as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)
    
    print(f"Backup extracted to: {EXTRACT_FOLDER}")

def restore_backup():
    """Main function to restore files from S3."""
    download_from_s3()
    decrypt_file()
    extract_backup()
    print("Backup restoration complete.")

if __name__ == "__main__":
    restore_backup()
