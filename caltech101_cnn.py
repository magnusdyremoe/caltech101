import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten


import numpy as np

from sklearn.model_selection import train_test_split

#Defining the model
model = Sequential([
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(32, (5,5), activation='relu'),
    MaxPooling2D(3, 3),
    Flatten(),
    Dense(32, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

#model.summary()

image_generator = ImageDataGenerator(rescale=1./255.,
                                        rotation_range=40,
                                        zoom_range=0.2,
                                        horizontal_flip=True,
                                        vertical_flip=True)

test_datagenerator = ImageDataGenerator( rescale=1./255. )

image_root = '../caltech101/101_objectcategories'
image_size = 224

data_gen = test_datagenerator.flow_from_directory(image_root,
                                                    target_size=(image_size, image_root),
                                                    batch_size=40,
                                                    shuffle=False,
                                                    class_mode=None)
                                        
num_images = len(data_gen.filenames)
num_epochs = int(np.ceil(num_images / 140))

print("Number of images: ", num_images)
print("Number of epochs: ", num_epochs)

train_data, test_data, 

model.compile(optimizer=RMSprop(lr=0.01),
                loss='binary_crossentropy',
                metrics = ['accuracy'])