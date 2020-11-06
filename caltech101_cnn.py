import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical



#Defining the model
model = Sequential([
    Conv2D(64, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(128, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(256, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Flatten(),
    Dense(256, activation='relu'),
    Dense(102, activation='softmax')
])

#model.summary()


train_root = '../caltech101/101_objectcategories/train'
val_root = '../caltech101/101_objectcategories/val'
image_size = 224

train_datagen = ImageDataGenerator(rescale=1./255.)

train_dataset = train_datagen.flow_from_directory(
    train_root,
    target_size=(image_size, image_size),
    batch_size=32,
    shuffle=False
)
                                        
train_images = len(train_dataset.filenames)
num_epochs = 10 #int(np.ceil(train_images / 140))
print("Number of training images: ", train_images)
print("Number of epochs: ", num_epochs)

val_datagen = ImageDataGenerator(rescale=1./255.)

val_dataset = val_datagen.flow_from_directory(
    val_root,
    target_size=(image_size, image_size),
    batch_size=32
)

val_images = len(val_dataset.filenames)
print("NUmber of validation images: ", val_images)

#print(train_dataset[0])
#print(val_dataset.classes.shape)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics = ['accuracy'],
)

val_labels = val_dataset.class_indices
print(val_labels)

## TRAINING
model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=num_epochs
)