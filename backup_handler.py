import schedule
import time
from s3_uploader import upload_to_s3
from encryption import compress_folder, encrypt_file

print("Backup Handler Started...")
input("Press Enter to exit...")


BUCKET_NAME = "backup-microservice"

def run_backup(folder_path):
    compressed_file = "backup_files"
    compress_folder(folder_path, compressed_file)   
    
    encrypted_file = encrypt_file(compressed_file + ".zip")
    
    upload_to_s3(encrypted_file, BUCKET_NAME)
    print("✅ Backup Process Completed")

schedule.every(20).seconds.do(run_backup, "C:\Z-Projects\XYZ")

while True:
    schedule.run_pending()
    time.sleep(1)
