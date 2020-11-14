# Visualizing data augmentation with Keras flow_from_directory

import os
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator


base_path = os.getcwd()
data_path = os.path.join(base_path, "101_ObjectCategories/train")
print(data_path)

data_gen = ImageDataGenerator(rescale=1./255.,
                            rotation_range=40,
                            width_shift_range=0.2,
                            height_shift_range=0.2,
                            horizontal_flip=True,
                            zoom_range=0.1,
                            shear_range=0.2,
                            )

dataset = data_gen.flow_from_directory(data_path)

augmented_images = [dataset[40][0][0] for i in range(5)]

fig, ax = plt.subplots(1, 5)
ax = ax.flatten()
for image, ax in zip(augmented_images, ax):
    ax.imshow(image)
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
plt.show()