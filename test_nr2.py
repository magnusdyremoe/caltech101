# Tested network nr 2

"""
#Defining the model
model = Sequential([
    Conv2D(64, (3,3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(128, (3,3), activation='relu', padding='same'),
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

epochs = 30
"""
import numpy as np
import matplotlib.pyplot as plt

epochs = np.linspace(1,8, num=8)
print(epochs)

train_loss = [3.4509, 0.7235, 0.0920, 0.0272, 0.0178, 0.0171, 0.0135, 0.0083]
train_acc = [0.2434, 0.7991, 0.9798, 0.9960, 0.9975, 0.9990, 0.9993, 0.9994]

val_loss = [2.3670, 2.5151, 3.3289, 3.3426, 3.5273, 3.5328, 3.3857, 3.42370]
val_acc = [0.4766, 0.5435, 0.5428, 0.5492, 0.5715, 0.5651, 0.5579, 0.5723]

plt.plot(epochs, train_acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and validation accuracy')
plt.figure()


plt.plot(epochs, train_loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")


plt.title('Training and validation loss')

plt.show()