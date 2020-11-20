"See read_me.md for how to."

import os
import numpy as np
import shutil

base_path = os.getcwd()
data_path = os.path.join(base_path, "101_ObjectCategories/train") 
categories = os.listdir(data_path)
val_path = os.path.join(base_path, "101_ObjectCategories/val")
test_path = os.path.join(base_path, "101_ObjectCategories/test")


for cat in categories:
    image_files = os.listdir(os.path.join(data_path, cat))
    
    # 75% training, 15% validation, 10% testing
    choices = np.random.choice([0, 1, 2], size=(len(image_files),), p=[.75, .15, 0.1])    
    for _f, choice in zip(image_files, choices):

        # Move to validation directory
        if choice == 1:
            origin_path = os.path.join(data_path, cat, _f)
            dest_dir = os.path.join(val_path, cat)
            dest_path = os.path.join(val_path, cat, _f)
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            shutil.move(origin_path, dest_path)
        
        # Move to test directory
        if choice == 2:
            origin_path = os.path.join(data_path, cat, _f)
            dest_dir = os.path.join(test_path, cat)
            dest_path = os.path.join(test_path, cat, _f)
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            shutil.move(origin_path, dest_path)
            