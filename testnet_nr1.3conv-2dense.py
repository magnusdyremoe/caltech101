"""
Test 1 with following network

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

"""
import matplotlib.pyplot as plt

epochs = [1,2,3,4,5,6,7,8]
train_loss = [4.9193, 4.3309, 3.7892, 3.3444, 2.8944, 2.2807, 1.5951, 0.8326]
train_acc = [0.0681, 0.1189, 0.2182, 0.3058, 0.3828, 0.4767, 0.6008, 0.7878]
val_loss = [4.5459, 3.9243, 3.6724, 3.2869, 3.0594, 3.0647, 3.0043, 3.5973]
val_acc = [0.0877, 0.1531, 0.2782, 0.3379, 0.3717, 0.4112, 0.4242, 0.4400]

plt.plot(epochs, train_acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and validation accuracy')
plt.figure()


plt.plot(epochs, train_loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")


plt.title('Training and validation loss')

plt.show()