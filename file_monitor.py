from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import threading
from backup_handler import run_backup

class BackupHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")
        run_backup(event.src_path)

def start_monitoring(folder_to_watch):
    observer = Observer()
    event_handler = BackupHandler()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_path = "C:\Z-Projects\XYZ"  # Change as needed
    thread = threading.Thread(target=start_monitoring, args=(folder_path,))
    thread.start()
