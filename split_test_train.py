"See read_me.md for how to."

import os
import numpy as np
import shutil

base_path = os.getcwd()
data_path = os.path.join(base_path, "101_ObjectCategories/train") 
categories = os.listdir(data_path)
test_path = os.path.join(base_path, "101_ObjectCategories/val")

for cat in categories:
    image_files = os.listdir(os.path.join(data_path, cat))
    choices = np.random.choice([0, 1], size=(len(image_files),), p=[.85, .15])    
    
    for _f, one in zip(image_files, choices):
        if one:
            origin_path = os.path.join(data_path, cat, _f)
            dest_dir = os.path.join(test_path, cat)
            dest_path = os.path.join(test_path, cat, _f)
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            shutil.move(origin_path, dest_path)
