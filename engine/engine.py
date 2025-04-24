import pandas as pd

import os
import requests
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime


dropzone_dir = './dropzone'


class FileHandler(FileSystemEventHandler):

    def __init__(self, file_name, file_ext):
        self.monitored_filename = file_name
        self.monitored_fileext = file_ext

    def on_created(self, event):
        # Check if the created file matches what we are monitoring
        if event.is_directory:
            return  # Ignore directories
        if os.path.basename(event.src_path) == f'{self.monitored_filename}.{self.monitored_fileext}':
            self.process_file(event.src_path)

    def process_file(self, file_path):
        print(f"Processing file: {file_path}")
        
        # Load property_records
        property_records = load_properties(file_path)
        update_database(property_records)

        upload_csv(file_path)

        # Move the processed file to ./processed
        self.move_file(file_path)

    def move_file(self, file_path):
        processed_dir = './processed'
        os.makedirs(processed_dir, exist_ok=True)  
        #datetime_string = datetime.now().strftime("%Y%m%d-%H%M%S")
        processed_fname = self.monitored_filename+\
        					datetime.now().strftime("%Y%m%d-%H%M%S")+\
        					self.monitored_fileext        
        shutil.move(file_path, os.path.join(processed_dir, processed_fname))
        print(f"Moved {file_path} to {processed_dir}/{processed_fname}")


def load_properties(csv_file_path):
    return pd.read_csv(csv_file_path)

def update_database(property_records):
    for record_num in range(len(property_records)):
	    for idx, col in enumerate(property_records.columns):
		    print (idx, col, property_records.values[record_num][idx])

def upload_csv(file_path):
    # url = 'http://127.0.0.1:8080/upload'
    url = 'http://svpserver5.ddns.net:8082/upload'
    
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print(f'Success: {response.text}')
    else:
        print(f'Error: {response.status_code} - {response.text}')

if __name__ == "__main__":
    # global dropzone_dir
    event_handler = FileHandler('calvaryproperty', 'csv')
    observer = Observer()
    observer.schedule(event_handler, path=dropzone_dir, recursive=False)
    try:
        observer.start()
        print(f"Monitoring {dropzone_dir} for changes...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()












