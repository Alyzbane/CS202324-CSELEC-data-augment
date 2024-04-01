# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:40:32 2024

@author: alyzbane
"""

import os
import zipfile
import matplotlib.pyplot as plt


def visualize(images, labels, rows=1, cols=1):
    """
    Visualize an image along with the given string of labels
    It will only accept a list of images that is compatible
    with the matplotlib.pyplot 

    Parameters
    ----------
    images : List[]
        Accept image of list that is compatible with matplotlib.pyplot
    labels : List[]
        Accept a l ist of string
    rows : Int, optional
        The row of subplots that will be displayed. The default is 1.
    cols : TYPE, optional
        The column of subplots that will be displayed. The default is 1.

    Returns
    -------
    None.

    """
    _, axs = plt.subplots(nrows=rows, ncols=cols)
    for pic, ax, label in zip(images, axs.flatten(), labels):
        ax.imshow(pic)
        ax.set_title(label)
        ax.axis('off')
    
    plt.savefig("default.png", dpi=150)
    
def create_dataset(src):
    """
    Takes an source path that will create a dataset assuming it has
    'labels' (subfolder) and  storing 'paths' in the dictionary

    Parameters
    ----------
    src : STRING
        Path of the directory to be read.

    Returns
    -------
    data : DICTIONARY
          Returns ['labels', 'paths'] of the data read from the source passed.

    """
    data = dict()
    data['labels'] = [] 
    #data['images'] = []
    data['paths'] = []

    # Read the specified  datasets of images in each subfolder with
    # their respective labels
    for root, subdir, files in os.walk(src):
        for class_name in subdir: 
            class_dir = os.path.join(root, class_name) 
            for filename in os.listdir(class_dir): 
                img_path = os.path.join(class_dir, filename)
                #with Image.open(img_path) as img:
                data['labels'].append(class_name)
                data['paths'].append(img_path)   
    return data
#############################
#           Folders 
#
############################

def create_folders(src, labels):
    os.makedirs(src, exist_ok=True)
    for i in labels:
        out_path = os.path.join(src, i)
        os.makedirs(out_path, exist_ok=True)
        
def create_folders_for_labels(output_dir, dataset_labels, extra_labels):
    """
    Creates folders for each label and each extra label inside their respective class folders.

    Parameters:
        output_dir (str): The main output directory.
        dataset_labels (list): List of labels.
        extra_labels (list): List of extra labels.

    Returns:
        None
    """
    for label in dataset_labels:
        label_folder = os.path.join(output_dir, label)
        create_folders(label_folder, extra_labels)
        
def zip_folder(folder_path, zip_path):
    """
    Compresses the entire folder at the specified path into a ZIP file.

    Parameters:
        folder_path (str): Path to the folder to be zipped.
        zip_path (str): Path to save the ZIP file.

    Returns:
        None
    """
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))        

def extract_zip(zip_path, output_path):
    """
    Extract the entire contents of zip file at the specified output path

    Parameters
    ----------
    zip_path : TYPE
        DESCRIPTION.
    output_path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    with zipfile.ZipFile(zip_path, 'r') as zip:
        # Print the contents of zip
        zip.printdir()
        print('Extracting the contents...')
        zip.extractall(output_path)
        print('Done!')
        
if __name__ == "__main__":
    pass