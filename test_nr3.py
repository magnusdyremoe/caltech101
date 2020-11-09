# Test nr 3

"""
#Defining the model
model = Sequential([
    Conv2D(8, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(16, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Flatten(),
    Dense(102, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics = ['accuracy'],
)

val_labels = val_dataset.class_indices
#print(val_labels)

## TRAINING
model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=num_epochs
)
"""

import numpy as np
import matplotlib.pyplot as plt

epochs = np.linspace(1,8, num=8)
print(epochs)

train_loss = [3.1112, 0.8332, 0.1482, 0.0367, 0.0153, 0.0113, 0.0150, 0.0139]
train_acc = [0.2592, 0.7895, 0.9720, 0.9968, 0.9972, 0.9997, 0.9979, 0.9990]

val_loss = [2.3210, 2.1586, 2.7196, 2.8015, 2.8493, 2.7057, 2.8649, 2.9565]
val_acc = [0.4881, 0.5356, 0.5485, 0.5572, 0.5537, 0.5557, 0.5558, 0.5514]

plt.plot(epochs, train_acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and validation accuracy')
plt.figure()


plt.plot(epochs, train_loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")


plt.title('Training and validation loss')

plt.show()