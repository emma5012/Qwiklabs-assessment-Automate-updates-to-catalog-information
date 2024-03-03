#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

input_folder = "supplier-data/images"

current_directory = os.getcwd()

for filename in os.listdir(os.path.join(current_directory, input_folder)):
    if filename.endswith(".jpeg"):
        file_path = os.path.join(current_directory, input_folder, filename)

        with open(file_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
