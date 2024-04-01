# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:53:22 2024

@author: alyzbane
"""

import os
import cv2
from utils import (
    create_dataset, 
    create_folders, 
    create_folders_for_labels, 
    zip_folder,
    extract_zip,
    )
import preprocess

path = r".\tree"
zpath = r".\FAITHBark.zip"
extract_zip(zpath, '.')

dataset = create_dataset(path)
IMG_SIZE = (223, 223)

output_dir = "output"
create_folders(output_dir, dataset['labels'])

extra_labels = ['grayscale', 'segment', 'cannyedge', 'convolution2d']

create_folders_for_labels(output_dir, dataset['labels'], extra_labels)

for path, subf in zip(dataset['paths'], dataset['labels']):
    
    image = cv2.imread(path)

    if image.shape != IMG_SIZE: # Verify the image is uniformed
        image = cv2.resize(image, IMG_SIZE)
        
    # Slice the string for filename
    start = path.rfind('\\')  # Windows path separator
    end = path.rfind ('.')  # Before the extension
    
    filename = path[start + 1 : end] + ".jpg"
    
    
    # Apply preprocessing to the image and save in corresponding subfolder
    for xlabel in extra_labels:
        output_subfolder = os.path.join(output_dir, subf, xlabel, filename)
        
        if xlabel == 'grayscale':
            processed_image = preprocess.grayscale(image)
            cv2.imwrite(output_subfolder, processed_image)
        elif xlabel == 'segment':
            processed_image = preprocess.segmentation(image)
            cv2.imwrite(output_subfolder, processed_image)
        elif xlabel == 'cannyedge':
            processed_image = preprocess.cannyedge(image)
            cv2.imwrite(output_subfolder, processed_image)
        elif xlabel == 'convolution2d':
            processed_image = preprocess.convolution2d(image)
            cv2.imwrite(output_subfolder, processed_image)
            
        print(f"Saved preprocess image {output_subfolder}")   
    
print(f"Augmented images created and saved in {output_dir}")
zip_folder(output_dir, 'output.zip')