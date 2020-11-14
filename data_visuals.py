# Visualize calteck 101 data set

import os
import matplotlib.pyplot as plt
import random
import cv2

base_path = os.getcwd()
data_path = os.path.join(base_path, "101_ObjectCategories/train")
categories_train = os.listdir(data_path)
test_path = os.path.join(base_path, "101_ObjectCategories/test")
categories_test = os.listdir(test_path)
val_path = os.path.join(base_path, "101_ObjectCategories/val")
categories_val = os.listdir(val_path)

assert categories_train == categories_test == categories_val, (
    "Not similar categories"
) 


images_in_class = {}
for cat in categories_train:
    image_files = os.listdir(os.path.join(data_path, cat))
    images_in_class[cat] = len(image_files)

for cat in categories_test:
    image_files = os.listdir(os.path.join(test_path, cat))
    images_in_class[cat] += len(image_files)

for cat in categories_val:
    image_files = os.listdir(os.path.join(val_path, cat))
    images_in_class[cat] += len(image_files)

"""
# Display number of images per object category
plt.figure(figsize=(12,5))
plt.bar(range(len(images_in_class)), list(images_in_class.values()), align='edge', width=0.8)
plt.xticks(range(len(images_in_class)), list(images_in_class.keys()), rotation='vertical', fontsize=8)
plt.tight_layout()
plt.show()
"""


# Visualize images in 4 randomly selected classes.
num_categories = 4
num_images = 4

random_categories = random.sample(list(images_in_class), num_categories)
print(random_categories)

fig, ax = plt.subplots(nrows=num_categories, ncols=num_images)

for i, category in enumerate(random_categories):
    folder_path = os.path.join(data_path, category)
    images = [img for img in os.listdir(folder_path)][:num_images]
    for j, image in enumerate(images):
        file_path = os.path.join(folder_path, image)
        selected_image = cv2.imread(file_path)
        selected_image = cv2.resize(selected_image, (100,100))
        selected_image = cv2.cvtColor(selected_image, cv2.COLOR_BGR2RGB)
        ax[i,j].imshow(selected_image)
        ax[i,j].set_xticks([])
        ax[i,j].set_yticks([])

        if j==0:
            ax[i,j].annotate(category, xy=(0, -0.5), xycoords=ax[i,j].yaxis.label, 
                            size='large', ha='right', va='center')

fig.tight_layout()
fig.show()
plt.show()

