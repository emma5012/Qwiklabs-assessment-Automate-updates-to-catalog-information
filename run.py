#! /usr/bin/env python3
import os
import requests
import json


post_url = "http://localhost/fruits/"
descriptions_directory = "supplier-data/descriptions"

for filename in os.listdir(descriptions_directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(descriptions_directory, filename)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        name = lines[0].strip()
        weight = int(lines[1].split()[0])  # drop "lbs" and convert it into an integer
        description = lines[2].strip()
        image_name = os.path.splitext(filename)[0] + ".jpeg"

        fruit_data = {
            "name": name,
            "weight": weight,
            "description": description,
            "image_name": image_name
        }

        json_data = json.dumps(fruit_data)

        response = requests.post(post_url, json=json_data)

        if response.status_code == 201:
            print(f"Data for {name} successfully uploaded.")
        else:
            print(f"Failed to upload data for {name}. Status code: {response.status_code}")
