# Visualize calteck 101 data set

import os
import matplotlib.pyplot as plt

base_path = os.getcwd()
data_path = os.path.join(base_path, "101_ObjectCategories/train")
categories_train = os.listdir(data_path)
test_path = os.path.join(base_path, "101_ObjectCategories/val")
categories_val = os.listdir(test_path)

if categories_train == categories_val:
    print("Same shit yo")

images_in_class = {}
for cat in categories_train:
    image_files = os.listdir(os.path.join(data_path, cat))
    images_in_class[cat] = len(image_files)

for cat in categories_val:
    image_files = os.listdir(os.path.join(test_path, cat))
    images_in_class[cat] += len(image_files)

plt.figure(figsize=(12,5))
plt.bar(range(len(images_in_class)), list(images_in_class.values()), align='edge', width=0.8)
plt.xticks(range(len(images_in_class)), list(images_in_class.keys()), rotation='vertical', fontsize=8)
plt.tight_layout()
plt.show()
