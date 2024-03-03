#!/usr/bin/env python3

import os
from PIL import Image

input_folder = "images"
output_folder = "changed_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".tiff"):
        input_path = os.path.join(input_folder, filename)

        tif_image = Image.open(input_path)
        rgb_image = tif_image.convert("RGB")
        resized_image = rgb_image.resize((600, 400))
        
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpeg")
        resized_image.save(output_path)

print("Image conversion complete")
