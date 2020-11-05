import numpy as np
import mnist
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical


## SETUP
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

print(train_images.shape) # (60000, 28, 28)
print(train_labels.shape) # (60000,)

# Normalise the images.
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

# Reshape the images.
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

## BUILDING THE MODEL
num_filters = 8
filter_size = 3
pool_size = 2

# Suggestions - 8, 12 filters; 12, 16 filters; 1 layer, 8 filters. 
model = Sequential([
    # First conv layer
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)), #only need input shape for first layer
    MaxPooling2D(pool_size=pool_size),

    # Second conv layer for flex
    Conv2D(12, filter_size),
    MaxPooling2D(pool_size=pool_size),

    # Flatten before softmax (Dense takes 1D array)
    Flatten(),
    Dense(10, activation='softmax'),
])

# Optional
model.summary()

model.compile(
    'adam', #optimiser
    loss='categorical_crossentropy', #loss for softmax
    metrics=['accuracy'], # we want to see this
)

## TRAINING
model.fit(
    # Training data
    train_images,

    # Labels
    to_categorical(train_labels), # to_categorical creates an array, with [0 .. 1 .. 0] at index given by test label

    epochs=5,

    # Check performance by setting this
    validation_data=(test_images, to_categorical(test_labels)), 
)




